import warnings

import numpy as np
import pandas as pd


def read_scalefile_gtkterm(mass_data_file: str, time_step: float = 0.295):
    """
    read_scalefile_gtkterm reads the scale data written by gtkterm

    Parameters
    ----------
    mass_data_file : str
        path to the mass file
    time_step : float, optional
        scale writing internal time step, by default 0.295. CARFEULL, the default value has been unprecisely calibrated.

    Returns
    -------
    time : numpy array
        time vector in seconds
    mass : numpy array
        mass vector in grams
    """
    mass_data = np.array(pd.read_csv(mass_data_file, delimiter=r"\n", engine="python")).squeeze()
    mass_data = np.array([m.replace("g", "").replace("Error", "nan").replace(r" ", "") for m in mass_data]).astype(
        "float"
    )
    time = np.arange(mass_data.size) * time_step
    warnings.warn(
        "!!! Be carefull when using the default time step, it has been unprecisely calibrated. You should use your own and check it !!!"
    )

    return time, mass_data
