## Here are the test functions.

import pytest
import numpy

from functions import check_genotypes, fixation_index, inbreeding_coefficient


# Function to test checks
def test_check_genotypes():

    # Normal use
    assert check_genotypes(["AA", "Aa", "aa"]) == ["AA", "Aa", "aa"]

    # Misuse cases
    with pytest.raises(ValueError):
        check_genotypes([])
    with pytest.raises(TypeError):
        check_genotypes(print)
    with pytest.raises(ValueError):
        check_genotypes(["AA", "Aa", "Aaa"])
    with pytest.raises(ValueError):
        check_genotypes(["", "", ""])


# Function to test inbreeding coefficient
def test_inbreeding_coefficient():

    # Tests with known values
    assert inbreeding_coefficient(["AA", "Aa", "aa"]) == pytest.approx(1 / 3)
    assert inbreeding_coefficient(["AA", "AA", "aa", "aa"]) == pytest.approx(1)
    assert inbreeding_coefficient(["AA", "Aa", "aa", "Aa"]) == pytest.approx(0)
    assert numpy.isnan(inbreeding_coefficient(["AA", "AA", "AA"]))
    assert numpy.isnan(inbreeding_coefficient(["aa", "aa", "aa"]))


# Function to test fixation index
def test_fixation_index():

    # Test fixation index
    assert fixation_index(["AA", "AA", "AA"], ["aa", "aa", "aa"]) == pytest.approx(1)
    assert fixation_index(["AA", "Aa", "aa"], ["aa", "Aa", "AA"]) == pytest.approx(0)
    assert fixation_index(["Aa", "Aa", "Aa"], ["Aa", "Aa", "Aa"]) == pytest.approx(0)
    assert fixation_index(["AA", "AA", "Aa", "Aa"], ["aa", "aa", "Aa", "Aa"]) == pytest.approx(0.25)
