## Here we check code coverage.

import sys
from pathlib import Path

import pytest

# NEW FILE PROVIDED

# Run the tests and generate a coverage report.
exit_code = pytest.main(
    [
        "-v",
        "--cov=functions",
        "--cov-report=term-missing",
        "--cov-report=html",
        "tests.py",
    ]
)

print("\nOpen this file in your browser to see coverage per function:")
print(Path("htmlcov/function_index.html").resolve())

sys.exit(exit_code)
