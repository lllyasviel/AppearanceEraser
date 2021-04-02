# Python Implementation of a very simple texture/illumination decomposition
# For reviewing purposes only. Please refer to main article for more details.

import numpy as np


def RGB2Luminance(image):
    T = image[:, :, 2] * 0.299 + image[:, :, 1] * 0.587 + image[:, :, 0] * 0.114
    return np.tile(T[:, :, None], [1, 1, 3])


def image_decomposition(smoothed_structure, original_image):
    luminance_smoothed_structure = RGB2Luminance(smoothed_structure)
    luminance_original_image = RGB2Luminance(original_image)
    simple_illumination_decomposition = luminance_original_image / luminance_smoothed_structure * 0.5
    return simple_illumination_decomposition
