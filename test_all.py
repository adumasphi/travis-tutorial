import numpy as np

def test_addition():
    assert 1 + 1 == 2

def test_soustraction():
    assert 1 - 1 == 0

def test_division():
    np.testing.assert_equal(3/2, 1.5)
