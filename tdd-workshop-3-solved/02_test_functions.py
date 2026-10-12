## Here we test some functions.

import sys
import pytest

# Run the tests
exit_code = pytest.main(["-v", "tests.py"])

# Check
sys.exit(exit_code)

# Hint: To see or edit the actual tests being run, have a look at tests.py.

## All tests green? Then they pass! (Red? Read the lines starting with E.)