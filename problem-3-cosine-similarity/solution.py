import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""
    dot = np.dot(a, b)
    a_norm, b_norm = np.linalg.norm(a), np.linalg.norm(b)

    if a_norm == 0 or b_norm == 0:
        raise ValueError

    return np.divide(dot, (a_norm * b_norm))
