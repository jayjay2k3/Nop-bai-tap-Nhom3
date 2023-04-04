import pytest
from src.index import independentFunction
from unittest.mock import patch
import os


# Một hàm test cơ bản có dạng:
def test_independentFunction_basic():
    assert independentFunction(True,True,True) == True


@pytest.mark.parametrize(
    "a, b, c, exprected_result",
    [
        (1, 1, 1, True),  # Test case 1
        (1, 2, 3, False),  # Test case 2
        (2, 3, 4, True),  # Test case 3
        (5, 6, 7, True),  # Test case 4
        (2, 3, 5, False),  # Test case 5
    ],
)
def test_independentFunction(a,b,c, exprected_result):
    assert independentFunction(a,b,c) == exprected_result
