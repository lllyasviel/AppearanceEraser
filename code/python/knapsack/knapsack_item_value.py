# Python Implementation of EAP knapsack item value computation.
# For reviewing purposes only. Please refer to main article for more details.

import sys
sys.path.append('..')

import numpy as np
from configs.config import *


# Corresponding to Eq. (8) in main article.
def computing_item_value(source_image, target_image):
    value_map = np.zeros(shape=(image_height, image_width), dtype=np.float32)
    H, W, C = source_image.shape
    padded_source_image = np.pad(source_image, ((1, 1), (1, 1), (0, 0)), 'symmetric')
    padded_target_image = np.pad(target_image, ((1, 1), (1, 1), (0, 0)), 'symmetric')
    for y_i in range(3):
        for x_i in range(3):
            for y_j in range(3):
                for x_j in range(3):
                    current_source_image = padded_source_image[y_i:y_i + H, x_i:x_i + W]
                    current_target_image = padded_target_image[y_j:y_j + H, x_j:x_j + W]
                    current_distance = current_source_image - current_target_image
                    current_distance = np.mean(np.square(current_distance), axis=2)
                    current_distance *= np.power(np.e, current_distance * 0.5)
                    value_map += current_distance
    return value_map

