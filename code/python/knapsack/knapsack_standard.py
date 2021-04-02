# Python Implementation of standard 0-1 knapsack algorithm.
# For reviewing purposes only. Please refer to main article for more details.

import numpy as np
from numba import njit


# A very standard 0-1 knapsack dynamic programming.
@njit
def knapsack_01_standard_optimal_inner_loop(n, c, w, v):
    value = [[0 for j in range(int(c) + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, int(c) + 1):
            value[i][j] = value[i - 1][j]
            if j >= w[i - 1] and value[i][j] < value[i - 1][int(j - w[i - 1])] + v[i - 1]:
                value[i][j] = value[i - 1][int(j - w[i - 1])] + v[i - 1]
    x = [0 for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][int(j)] > value[i - 1][int(j)]:
            x[i - 1] = 1
            j -= w[i - 1]
    return x


# Wrapping of 0-1 knapsack dynamic programming.
def knapsack_01_standard_optimal(all_weights, all_values, knapsack_capability):
    assert all_weights.shape == all_values.shape
    assert knapsack_capability > 0
    c = knapsack_capability
    w = all_weights.tolist()
    v = all_values.tolist()
    n = len(w)
    x = knapsack_01_standard_optimal_inner_loop(n, c, w, v)
    return np.array(x, dtype=np.float32)


# You may directly test this knapsack implementation using the following codes.

# test_knapsack_capability = 200.5
# test_weights = np.array([2.4, 2.6, 3.2, 1.2, 5.7, 2.9])
# test_values = np.array([2.7, 3.2, 1.6, 5.3, 4.3, 3.1])
# test_result = knapsack_01_standard_optimal(test_weights, test_values, test_knapsack_capability)
# print(test_result)
