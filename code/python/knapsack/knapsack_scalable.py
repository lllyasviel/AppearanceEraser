# Python Implementation of a greedy 0-1 knapsack algorithm.
# For reviewing purposes only. Please refer to main article for more details.

# This algorithm can tackle very large knapsack problems in very short time.
# This is a greedy algorithm. It is fast and scalable.
# The accuracy is very good though it is an approximation.


import numpy as np
from numba import njit

from .knapsack_standard import knapsack_01_standard_optimal


N_greedy_degree = 50  # Please refer to supplement material for details of N_greedy_degree.


@ njit
def get_key_index(sorted_items, knapsack_capability):
    current_value = 0
    for i in range(sorted_items.shape[0]):
        current_value += sorted_items[i, 1]
        if current_value > knapsack_capability:
            return i
    return sorted_items.shape[0]


def knapsack_01_greedy_scalable(all_weights, all_values, knapsack_capability, simulated_annealing):
    assert all_weights.shape == all_values.shape
    assert knapsack_capability > 0
    # Greedy search.
    all_density = (all_values + 1e-3) / (all_weights + 1e-3)
    all_items = np.stack([all_values, all_weights, np.arange(all_values.shape[0])], axis=1)
    sorted_items = all_items[np.argsort(all_density)][::-1]
    key_index = get_key_index(sorted_items, knapsack_capability)
    key_value = sorted_items[key_index, 0]
    # Transform the data space.
    x = np.array([0 for i in range(all_values.shape[0])], dtype=np.float32)
    for i in range(key_index):
        x[i] = 1
    # Only perform standard 0-1 knapsack on some interested items.
    interest_items = sorted_items[key_index - N_greedy_degree: key_index + N_greedy_degree]
    interest_capability = knapsack_capability - np.sum(sorted_items[:key_index - N_greedy_degree, 1])
    x[key_index - N_greedy_degree: key_index + N_greedy_degree] = \
        knapsack_01_standard_optimal(interest_items[:, 1], interest_items[:, 0], interest_capability)
    # Transform the data space back.
    z = np.zeros_like(x)
    for i in range(all_values.shape[0]):
        if x[i] == 1:
            z[int(sorted_items[i, 2])] = 1
    # Introducing simulated annealing algorithm for stabilized and accurate convergence.
    r1 = np.random.uniform(low=0.0, high=1.0, size=z.shape)
    r2 = np.random.uniform(low=0.0, high=1.0, size=z.shape)
    normed_value = 0.5 + (all_values / key_value * 2.0 - 0.5) * (1.0 - simulated_annealing)
    r3 = np.where(np.less_equal(r1, normed_value), np.zeros_like(z), np.ones_like(z))
    r4 = np.where(np.less(r2, simulated_annealing ** 2.0), r3, z)
    return r4

# You may directly test this implementation using the following codes.

# test_knapsack_capability = 20480
# test_weights = np.random.uniform(low=0.5, high=50.0, size=(20000, ))
# test_values = np.random.uniform(low=0.5, high=50.0, size=(20000, ))
# test_result = knapsack_01_greedy_scalable(test_weights, test_values, test_knapsack_capability, 0)
# print(test_result)
