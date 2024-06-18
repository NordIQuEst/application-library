#!/usr/bin/env python3.9
# coding: utf-8
# This code is part of Tergite
#
# (C) Copyright Axel Andersson 2022
# (C) Copyright Martin Ahindura 2024
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import time
import numpy as np
import requests
import matplotlib.pyplot as plt
from uuid import uuid4 as uuid
from qiskit.providers.jobstatus import JobStatus
from tergite_qiskit_connector.providers.tergite import Tergite
from tergite_qiskit_connector.providers.tergite.provider_account import ProviderAccount
from tqdm.auto import tqdm
from pathlib import Path
from os import makedirs, environ
from os import listdir
from datetime import datetime
from shutil import move


API_URL = environ.get("QAL9000_API_URL", default="https://api.qal9000.se")
BCC_URL = environ.get("QAL9000_BCC_URL")
API_TOKEN = environ.get("QAL9000_API_TOKEN")
# the name of this service. For your own bookkeeping.
SERVICE_NAME = "local"

folder = Path("demo_qmc_frames").resolve()

def save_old_frames():
    global folder
    saved_folder = folder / "saved_animations"
    makedirs(saved_folder, exist_ok = True)

    old_frames = [ f for f in listdir(folder) if f.endswith(".jpg")]

    if len(old_frames):
        now_time = datetime.now()
        mstr = now_time.strftime("%Y%m%d%H%M%S")
        new_dir = saved_folder / mstr
        makedirs(new_dir, exist_ok = True)
        for f in old_frames:
            move(folder / f, new_dir / f)

save_old_frames()

#-------------------------- HELPERS FOR GENERATING FIGURE ----------------------------------
def f(x):
    return np.sqrt(1 - x**2)

# hitmiss estimator, given input points
def qmc_estimate(fn: callable, U : np.ndarray) -> float:
    estimate = np.mean(
        U[:, 1] <= fn(U[:, 0])
    )  # <- This is the estimator for integral value
    return estimate

def plot_labels_etc(ax: object):
    text_settings = dict(fontsize = 23)
    ax.set_title("Quantum Monte Carlo", **text_settings)
    ax.plot(np.linspace(0, 1, 1000), f(np.linspace(0, 1, 1000)), lw=3.5, zorder=99)
    ax.set_ylabel("f(x)", **text_settings)
    ax.set_xlabel("x", **text_settings)
    ax.grid(zorder=-99, alpha=0.5)
    ax.tick_params(axis="both", which="minor", labelsize=text_settings["fontsize"])
    ax.tick_params(axis="both", which="major", labelsize=text_settings["fontsize"])

# plots a textbox
def plot_estimate(ax: object, estimate: float):
    textstr = "$\hat\pi = {:10.5f}$".format(estimate)
    props = dict(boxstyle="round", facecolor="wheat", alpha=1)
    # place a text box in upper left in axes coords
    ax.text(
        0.15,
        0.15,
        textstr,
        transform=ax.transAxes,
        verticalalignment="top",
        bbox=props,
        fontsize=25,
    )

# plots points with formatting
def plot_samples(ax: object, samples: np.array, marker: str = "o"):
    inside = np.sqrt(samples[:, 0] ** 2 + samples[:, 1] ** 2) < 1
    ax.scatter(samples[inside, 0], samples[inside, 1], color="C1", marker = marker)
    ax.scatter(samples[~inside, 0], samples[~inside, 1], color="C2", marker = marker)

#-------------------------- BACKEND SETTINGS ----------------------------------
# vm_url = "http://qtl-axean.mc2.chalmers.se"
# mss_url = vm_url + ":8002"
# bcc_url = vm_url + ":8000"
account = ProviderAccount(service_name=SERVICE_NAME, url=API_URL, token=API_TOKEN)
chalmers = Tergite.use_provider_account(account)
backend = chalmers.get_backend("Nov7")
print(f"Connected to backend: {backend.name}")

#-------------------------- COMPUTING THE FRAMES ----------------------------------

points = np.asarray([[],[]]).T
job_ids = list(str(uuid()) for _ in range(15))

def compute_new_frame(j: int):
    global points
    global job_ids
    job_id = job_ids[j]

    fig, ax = plt.subplots(figsize=(7.6,7.6))

    # queue job on backend
    bcc_response = requests.get(bcc_url + "/rng/" + job_id)
    assert bcc_response.ok

    # wait for job to complete, blocking REST API call chain
    mss_response = requests.get(API_URL + "/rng/" + job_id)
    assert mss_response.ok
    data = mss_response.json()

    # split obtained numbers into two disjoint subsets
    N = data["N"] // 2
    X = np.asarray(data["numbers"][:N]).astype(float)  # first N are X coordinate
    Y = np.asarray(data["numbers"][N : (N + N)]).astype(float)  # second N are Y coordinate

    # these numbers are random 32-bit integers in the range [-2**31, 2**31 - 1]
    # so we want to convert them to floats in the range [0,1]
    X += 2**31
    Y += 2**31

    X *= 2**-32
    Y *= 2**-32

    # concatenate points obtained
    U = np.zeros((N,2))
    U[:,0] = X
    U[:,1] = Y
    points = np.concatenate((points, U))
    est = qmc_estimate(f, points)

    # create figure and save
    plot_labels_etc(ax)
    plot_samples(ax, points)
    plot_estimate(ax, est*4)

    fig.savefig(folder / f"frame{j}.jpg", dpi=300, bbox_inches="tight")

for j in tqdm(range(len(job_ids)), desc = "Quantum Monte Carlo"):
    compute_new_frame(j)
