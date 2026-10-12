## Here we try some functions.

import random

from functions import check_genotypes, fixation_index, inbreeding_coefficient

# Sample fake genotypes
genotypes = random.choices(["aa", "Aa", "AA"], k=100)

# Check input
print(check_genotypes(genotypes))

# Compute inbreeding coefficient
print(inbreeding_coefficient(genotypes))

# Other genotypes
other_genotypes = random.choices(["aa", "Aa", "AA"], k=100)

# Compute fixation index
print(fixation_index(genotypes, other_genotypes))

## Use this script to try out your functions with various inputs, see
## how they behave and check whether the output makes sense. What if there
## was a way to automatize that process?
