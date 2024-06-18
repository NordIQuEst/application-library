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

import contextlib
import time
import matplotlib.pyplot as plt
import numpy as np
import qiskit.circuit as circuit
import qiskit.compiler as compiler

with contextlib.redirect_stderr(None):
    from qiskit.ignis.verification.tomography import StateTomographyFitter
    from qiskit.ignis.verification.tomography import state_tomography_circuits

from qiskit.providers.jobstatus import JobStatus
from qiskit.visualization import plot_bloch_multivector
from tqdm.auto import tqdm

from tergite_qiskit_connector.providers.tergite import Tergite
from tergite_qiskit_connector.providers.tergite.provider_account import ProviderAccount

from pathlib import Path
from os import makedirs, listdir, environ
from datetime import datetime
from shutil import move

API_URL = environ.get("QAL9000_API_URL", default="https://api.qal9000.se")
API_TOKEN = environ.get("QAL9000_API_TOKEN")
# the name of this service. For your own bookkeeping.
SERVICE_NAME = "local"

folder = Path("demo_bloch_frames").resolve()

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

#----------------------------------------------------------------------------

account = ProviderAccount(service_name=SERVICE_NAME, url=API_URL, token=API_TOKEN)
chalmers = Tergite.use_provider_account(account)
backend = chalmers.get_backend("Nov7")
backend.set_options(shots=2000)

print(f"Loaded backend {backend.name} (QAL 9000)")

thetadef = -1 * np.asarray([0, np.pi/2, np.pi])

def tomog_circs(theta):
    q = circuit.QuantumRegister(1)
    circ = circuit.QuantumCircuit(q)
    circ.barrier([0])
    circ.reset([0])

    circ.rx(theta, q[0])

    return state_tomography_circuits(circ, [q[0]])

print("Transpiling...")
with contextlib.redirect_stderr(None):
    precomputed_tomog_circs = [
        compiler.transpile(tomog_circs(theta), backend=backend)
        for theta in thetadef
    ]

def compute_new_frame(j: int):

    job = backend.run(precomputed_tomog_circs[j], meas_level=2, meas_return="single")
    while job.status() != JobStatus.DONE:
        time.sleep(1)  # blocking wait

    # fit state vector when result is ready
    fitter = StateTomographyFitter(job.result(), precomputed_tomog_circs[j])

    density_matrix = fitter.fit(method="lstsq")

    # compute frame and save to main memory
    _tmp = plot_bloch_multivector(
        density_matrix, reverse_bits=True, filename= folder / f"frame{j}.jpg"
    )
    plt.close(_tmp) # close returned figure

# progress bar
for j in tqdm(range(len(thetadef)), desc = "Reconstructing qubit state"):
    compute_new_frame(j)
