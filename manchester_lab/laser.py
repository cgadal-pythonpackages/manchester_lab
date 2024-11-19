from io import StringIO

import cv2
import numpy as np

from manchester_lab._sylk_parser import SylkParser

OFFSET_Z = {"large": 286.16, "small": 86.16}


def slk_to_csv(file_path: str, path_ouput: str = None):
    """
    slk_to_csv converts the .slk files given as export by the micro-epsilon software into a csv file. Can be used to check the output of `laseravi_to_npy`.

    NOTE: the export via the software has been seen to miss some time stamps, so be carefull when you cant to make a frame to frame comparison.

    CREDITS: This function uses the parsers sylk_parser.py and 'sylk.py' taken from https://github.com/majerteam/sylk_parser

    Parameters
    ----------
    file_path : str
        path to file
    path_ouput : str
        ouput file path. Default is None, meaning that the output file is written where the input file is stored, with the same name, only changing the extension.
    """
    parser = SylkParser(file_path)
    fbuf = StringIO()
    parser.to_csv(fbuf)

    test_results = fbuf.getvalue().replace('"', "")
    if path_ouput is None:
        path_ouput = file_path.replace("slk", "csv")

    with open(path_ouput, "w") as f:
        f.writelines(test_results)


def laseravi_to_npy(file_path: str, laser: str = "small"):
    """
    laseravi_to_npy read the .avi fiel from the micro-epsilon laser scanners into a numpy array.

    Parameters
    ----------
    file_path : str
        AVI file path
    laser : str, optional
        laser model, should be 'large' or 'small' (default is "small"). The difference between the two is only a vertical absolute shift. It should not matter if any background substraction is done.
    Returns
    -------
    numpy array
        _return an array of size (Nframe, Npoints, 2), containing the [x,z] data. Hence, data[100, 200, :] is the 100th frame, (x, y) values of the 200th mes. point
    """
    # %%%%%
    cam = cv2.VideoCapture(file_path)

    ret = True
    data = []

    while ret:
        ret, frame = cam.read()
        if ret:
            frame = frame.astype(float)[..., 0]
            # ### check condition to see if the measurements is valid, instead put Nan (correspond to non-exported lines in slk files)
            mask = frame[:, 4] == 0
            frame[mask, :] = np.nan

            # ### magic conversion
            x = (256 * frame[:, 4] + frame[:, 5]) / 200 - 163.84
            z = (256 * frame[:, 6] + frame[:, 7]) / 200 + OFFSET_Z[laser]
            data.append(np.array([x, z]).T)

    data = np.array(data)
    return data
