# Python Implementation of a very LAB transform

import numpy as np


def RGB2YUV(x):
    R = x[:, :, 0]
    G = x[:, :, 1]
    B = x[:, :, 2]
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    U = 0.492 * (B - Y) + 0.5
    V = 0.877 * (R - Y) + 0.5
    return np.stack([Y, U, V], axis=2)


def YUV2RGB(x):
    Y = x[:, :, 0]
    U = x[:, :, 1]
    V = x[:, :, 2]
    R = Y + 1.140 * (V - 0.5)
    G = Y - 0.394 * (U - 0.5) - 0.581 * (V - 0.5)
    B = Y + 2.032 * (U - 0.5)
    return np.stack([R, G, B], axis=2)