import pytest
from jackie_utils.math_utils import moving_average

def test_moving_average_basic():
    assert moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]

def test_moving_average_invalid_window():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 0)

def test_moving_average_window_too_large():
    with pytest.raises(ValueError):
        moving_average([1, 2], 3)