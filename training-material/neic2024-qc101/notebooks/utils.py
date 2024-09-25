import os
import json
import requests


import matplotlib.pyplot as plt
from iqm.iqm_client import IQMClient


def get_calibration_data(
    client: IQMClient, calibration_set_id=None, filename: str = None
):
    """
    Return the calibration data and figures of merit using IQMClient.
    Optionally you can input a calibration set id (UUID) to query historical results
    Optionally save the response to a json file, if filename is provided
    """
    headers = {"User-Agent": client._signature}
    bearer_token = client._get_bearer_token()
    headers["Authorization"] = bearer_token

    if calibration_set_id:
        url = os.path.join(client._base_url, "calibration/metrics/", calibration_set_id)
    else:
        url = os.path.join(client._base_url, "calibration/metrics/latest")

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # will raise an HTTPError if the response was not ok

    data = response.json()
    data_str = json.dumps(data, indent=4)

    if filename:
        with open(filename, "w") as f:
            f.write(data_str)
        print(f"Data saved to {filename}")

    return data


def plot_metrics(
    metric: str, title: str, ylabel: str, xlabel: str, data: dict, limits: list = []
):
    # Initialize lists to store the values and labels
    values = []
    labels = []

    # Iterate over the calibration data and collect values and labels based on the metric
    for key, metric_data in data["metrics"].items():
        if key.endswith(metric):
            values.append(float(metric_data["value"]))
            # Extract the qubit label from the key
            labels.append(key.split(".")[0])

    # Check if values were found for the given metric
    if not values:
        return f"{metric} not in quality metrics set!"

    # Set the width and gap between the bars
    bar_width = 0.4
    # Calculate the positions of the bars
    positions = range(len(values))
    # Plot the values with labels
    plt.bar(positions, values, width=bar_width, tick_label=labels)

    if len(limits) == 2:
        plt.ylim(limits)

    plt.grid(axis="y")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.show()
