# Python Implementation of EAP based TV smoothing (or called ETV in paper).
# For reviewing purposes only. Please refer to main article for more details.
# This code can be modified to apply other smoothing energy. Please refer to supplement material for details.
# This code will automatically try different knapsack capability and output all results for evaluation.

# Note that this code is very slow because we are trying to compute ALL configurations.
# This code can be significantly speeded up if you only need one configuration.
# Besides, this TV smoothing is implemented using TensorFlow and Adam, and it is slower than MATLAB.
# Finally, this reviewing code is only improved for readableness, and not optimized for speed.

# THE NTV RESULTS OF THIS CODE SHOULD ONLY BE COMPARED TO TV SMOOTHING.

# Import all libraries.
import os
import cv2
from utils.CIELAB import *
from configs.config import *
from utils.decomposition import *
from knapsack.knapsack_scalable import *
from knapsack.knapsack_item_value import *
from knapsack.knapsack_item_weight import *
from smoothing.TV_smoothing_tensorflow import *

# Read image and convert the data type.
image = cv2.imread(image_name)
image_uint8 = image.copy()
image_float32 = image.astype(np.float32) / 255.0

for knapsack_capability in [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.95][::-1]:  # Some possible knapsack capabilities.
    print('Knapsack Capability = ' + str(knapsack_capability))

    # Generating some random noise.
    random_noise = np.random.uniform(low=0.0, high=1.0, size=(image_height, image_width))
    random_noise[random_noise < 0.5] = 0.0
    random_noise[random_noise > 0.0] = 1.0

    # Randomly initialize the erasing set.
    erasing_map = random_noise
    non_erasing_map = 1.0 - random_noise

    # Actual Iterations. We carry on 10 iterations for all configurations.
    for iteration in range(10):
        # Perform smoothing
        smoothed_result = total_variation_smoothing(image_float32, erasing_map)

        # Visualize some simple and basic image decomposition.
        image_decomposition_result = image_decomposition(smoothed_result, image_float32)

        # Computing item value for knapsack algorithm.
        value_map = computing_item_value(RGB2YUV(image_float32), RGB2YUV(smoothed_result))
        all_value = np.reshape(value_map, (image_height * image_width,))

        # Computing item weights for knapsack algorithm.
        weight_map = computing_item_weight(RGB2YUV(smoothed_result))
        all_weight = np.reshape(weight_map, (image_height * image_width,))

        # Solve 0-1 knapsack.
        knapsack_result = knapsack_01_greedy_scalable(
            all_weights=all_weight,
            all_values=all_value,
            knapsack_capability=image_height * image_width * knapsack_capability,
            simulated_annealing=1.0 - float(iteration) / 9.0
        )

        # Interpreting supporting positions and non-supporting positions.
        non_erasing_map = np.reshape(knapsack_result, (image_height, image_width))
        erasing_map = 1.0 - non_erasing_map

        # Visualize Points
        visualized_points = np.zeros_like(image_float32)
        visualized_points[:, :, 1] = non_erasing_map

        # Writing results.
        path = './outputs/capability_' + ('%.2f' % knapsack_capability)
        name = path + '/iteration_' + str(iteration) + '.png'
        os.makedirs(path, exist_ok=True)
        cv2.imwrite(name, (np.concatenate([
            image_float32,
            smoothed_result,
            visualized_points,
            image_decomposition_result
        ], axis=1) * 255.0).clip(0, 255).astype(np.uint8))
        print('Writing: ' + name)
