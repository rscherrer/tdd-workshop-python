## Here we try some functions.

import random

from functions import inbreeding_coefficient

# Sample fake genotypes
genotypes = random.choices(["aa", "Aa", "AA"], k=100)

# Compute inbreeding coefficient
print(inbreeding_coefficient(genotypes))

## Use this script to try out your functions with various inputs, see
## how they behave and check whether the output makes sense. What if there
## was a way to automatize that process?
