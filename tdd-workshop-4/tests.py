## Here are the test functions.

import pytest
import numpy

from functions import inbreeding_coefficient


def test_inbreeding_coefficient():
    assert inbreeding_coefficient(["AA", "Aa", "aa"]) == pytest.approx(1 / 3)
    assert inbreeding_coefficient(["AA", "AA", "aa", "aa"]) == pytest.approx(1)
    assert inbreeding_coefficient(["AA", "Aa", "aa", "Aa"]) == pytest.approx(0)
    assert numpy.isnan(inbreeding_coefficient(["AA", "AA", "AA"]))
    assert numpy.isnan(inbreeding_coefficient(["aa", "aa", "aa"]))
   
    # Test that error when empty input    
    with pytest.raises(ValueError):
        inbreeding_coefficient([])
        
    # Test that error when not a list of genotypes
    with pytest.raises(TypeError):
        inbreeding_coefficient(print)
        
    # Test that error when wrong ploidy
    with pytest.raises(ValueError):
        inbreeding_coefficient(["AAA", "Aa", "aa"])
        
    # NEW TEST ADDED WITH EMPTY GENOTYPE
    with pytest.raises(ValueError):
        inbreeding_coefficient(["AA", "", "aa"])