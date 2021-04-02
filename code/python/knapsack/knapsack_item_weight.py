# Python Implementation of EAP knapsack item weight computation.
# For reviewing purposes only. Please refer to main article for more details.

import sys
sys.path.append('..')

import numpy as np
from configs.config import *


# Corresponding to Eq. (9) in main article.
def computing_item_weight(source_image):
    weight_map = np.ones(shape=(image_height, image_width), dtype=np.float32)
    H, W, C = source_image.shape
    padded_source_image = np.pad(source_image, ((1, 1), (1, 1), (0, 0)), 'symmetric')
    for y_i in range(3):
        for x_i in range(3):
            for y_j in range(3):
                for x_j in range(3):
                    current_source_i = padded_source_image[y_i:y_i + H, x_i:x_i + W]
                    current_source_j = padded_source_image[y_j:y_j + H, x_j:x_j + W]
                    current_distance = current_source_i - current_source_j
                    current_distance = np.mean(np.square(current_distance), axis=2)
                    weight_map += current_distance * 0.25
    return weight_map

