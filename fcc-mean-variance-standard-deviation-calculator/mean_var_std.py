import numpy as np

def calculate(numbers: list) -> dict:
    """
    Outputs the mean, variance, standard deviation, max, min and
    sum of the rows, columns, and elements in a 3 x 3 matrix.
    """

    if len(numbers) < 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers, dtype=float).reshape((3, 3))

    means = [
        np.mean(matrix, axis=0).tolist(),
        np.mean(matrix, axis=1).tolist(),
        np.mean(matrix)
    ]
    variances = [
        np.var(matrix, axis=0).tolist(),
        np.var(matrix, axis=1).tolist(),
        np.var(matrix)
    ]
    standard_deviations = [
        np.std(matrix, axis=0).tolist(),
        np.std(matrix, axis=1).tolist(),
        np.std(matrix)
    ]
    maxs = [
        np.amax(matrix, axis=0).tolist(),
        np.amax(matrix, axis=1).tolist(),
        np.amax(matrix)
    ]
    mins = [
        np.amin(matrix, axis=0).tolist(),
        np.amin(matrix, axis=1).tolist(),
        np.amin(matrix)
    ]
    sums = [
        np.sum(matrix, axis=0).tolist(),
        np.sum(matrix, axis=1).tolist(),
        np.sum(matrix)
    ]

    calculations = {
        "mean": means,
        "variance": variances,
        "standard deviation": standard_deviations,
        "max": maxs,
        "min": mins,
        "sum": sums
    }

    return calculations
