import numpy as np

def create_array():
    return np.zeros(shape=(3,3))

def test_create_array():
    assert np.array_equal(create_array(), np.zeros(shape=(3,3))