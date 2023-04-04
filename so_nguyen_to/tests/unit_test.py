import pytest
from src.index import independentFunction
from unittest.mock import patch
import os


def test_independentFunction_basic():
    assert independentFunction(2) == True

@pytest.mark.parametrize(
    "a, exprected_result",
    [
        (1, False),  # Test case 1
        (2, True),  # Test case 2
        (4, False),  # Test case 3
        (5, True),  # Test case 4   
        (9, False),  # Test case 5   
    ],
)
def test_independentFunction(a, exprected_result):
    assert independentFunction(a) == exprected_result
