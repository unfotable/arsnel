"""numpy: fast arrays, broadcasting, masks and axis operations."""

# requires: numpy

import numpy as np

a = np.arange(6).reshape(2, 3)
print(a, a.shape, a.dtype)
print(a * 10 + 1)  # vectorised: no Python loop
print(a + np.array([100, 200, 300]))  # broadcasting a row
print(a.sum(), a.sum(axis=0), a.mean(axis=1))
print(a[a % 2 == 0])  # boolean mask
print(np.linspace(0, 1, 5))

loop_result = [x * x for x in range(1000)]
vector_result = np.arange(1000) ** 2
print(bool((np.array(loop_result) == vector_result).all()))
