import numpy as np
import pytest


def test_create_array():
    from pysample import create_array

    assert np.array_equal(create_array(), np.zeros(shape=(3, 3)))


def test_create_rand_array():
    from pysample import create_rand_array

    test_mean = 5
    test_std = 1
    test_shape = (3, 3)

    arr = create_rand_array(test_mean, test_std, test_shape)
    assert arr.mean() == pytest.approx(test_mean, 0.1)
    assert arr.std() == pytest.approx(test_std, 0.5)
    assert arr.shape == test_shape
