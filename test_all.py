import numpy as np

def test_addition():
    assert 1 + 1 == 2

def test_soustraction():
    assert 1 - 1 == 0

def test_division():
    np.testing.assert_equal(3./2, 1.5)

def test_numpy_partition():
    input_arr = np.array([3, 2, -1, 10])
    partitioned = np.partition(input_arr, 1)
    assert partitioned[1] == 2
    
def test_numpy_partition():
    input_arr = np.array([3, 2, -1, 10])
    np.testing.assert_array_equal(input_arr, [3, 2, -1, 10])
