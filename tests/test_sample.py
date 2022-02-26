import numpy as np


def test_create_array():
    from pysample.sample import create_array

    assert np.array_equal(create_array(), np.zeros(shape=(3, 3)))
