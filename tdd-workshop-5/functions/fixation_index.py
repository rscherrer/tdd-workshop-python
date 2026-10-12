from collections import Counter

import numpy as np

from .check_genotypes import check_genotypes


def fixation_index(genotypes1, genotypes2):
    """Calculate the fixation index between two populations.

    genotypes1, genotypes2: lists of genotypes (e.g., ["AA", "Aa", "aa"])
    """

    # Check and convert to string if needed
    genotypes1 = [str(genotype) for genotype in check_genotypes(genotypes1)]
    genotypes2 = [str(genotype) for genotype in check_genotypes(genotypes2)]

    # ...
    
    # COMPLETE HERE