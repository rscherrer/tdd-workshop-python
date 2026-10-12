## Here are the test functions.

import pytest

from functions import inbreeding_coefficient


def test_inbreeding_coefficient():
    assert inbreeding_coefficient(["AA", "Aa", "aa"]) == pytest.approx(1 / 3)
    assert inbreeding_coefficient(["AA", "AA", "aa", "aa"]) == pytest.approx(1)
    assert inbreeding_coefficient(["AA", "Aa", "aa", "Aa"]) == pytest.approx(0)
