from collections import Counter

import numpy as np

from .check_genotypes import check_genotypes


def _expected_heterozygosity(genotypes):
    """Expected heterozygosity from the allele frequencies of a list of genotypes."""

    # Extract alleles and compute allele frequencies
    counts = Counter(allele for genotype in genotypes for allele in genotype)
    total = sum(counts.values())

    return 1 - sum((count / total) ** 2 for count in counts.values())


def fixation_index(genotypes1, genotypes2):
    """Calculate the fixation index between two populations.

    genotypes1, genotypes2: lists of genotypes (e.g., ["AA", "Aa", "aa"])
    """

    # Check and convert to string if needed
    genotypes1 = [str(genotype) for genotype in check_genotypes(genotypes1)]
    genotypes2 = [str(genotype) for genotype in check_genotypes(genotypes2)]

    # Total expected heterozygosity
    Ht = _expected_heterozygosity(genotypes1 + genotypes2)

    # Average expected heterozygosity within populations
    Hs = (
        _expected_heterozygosity(genotypes1) + _expected_heterozygosity(genotypes2)
    ) / 2

    # Fixation index
    return np.nan if Ht == 0 else (Ht - Hs) / Ht
