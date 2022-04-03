"""
Pysample - Python library to test GitHub Actions and Sphinx/ReadTheDocs.
"""

import numpy as np


def create_array():
    """Return a 3x3 np.ndarray of zeroes.

    :return: 3x3 np.ndarray of zeroes
    :rtype: np.ndarray
    """
    return np.zeros(shape=(3, 3))


def create_rand_array(mean: float = 0.0, stdev: float = 1.0, shape: tuple = (3, 3)):
    """Creates an ndarray with the given shape, mean, and standard deviation.

    :param mean: mean of the array, defaults to 0.0
    :type mean: float, optional
    :param stdev: standard deviation of the array, defaults to 1.0
    :type stdev: float, optional
    :param shape: shape of the array, defaults to (3, 3)
    :type shape: tuple, optional
    :return: ndarray of the given shape with values equal to mean and stdev
    :rtype: np.ndarray
    """

    arr = np.zeros(shape=shape)

    return np.random.normal(loc=mean, scale=stdev, size=arr.size).reshape(arr.shape)
