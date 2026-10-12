from collections import Counter

import numpy as np

from .check_genotypes import check_genotypes


def inbreeding_coefficient(genotypes):
    """Calculate the inbreeding coefficient.

    genotypes: list of genotypes (e.g., ["AA", "Aa", "aa"])
    """

    # Check and convert to string if needed
    genotypes = [str(genotype) for genotype in check_genotypes(genotypes)]

    # Count alleles and compute allele frequencies
    counts = Counter(allele for genotype in genotypes for allele in genotype)
    total = sum(counts.values())
    frequencies = [count / total for count in counts.values()]

    # Compute expected heterozygosity
    He = 1 - sum(f ** 2 for f in frequencies)

    # Find heterozygotes
    def is_heterozygous(genotype):

        # Split alleles
        alleles = list(genotype)

        # Is it heterozygous?
        return any(allele != alleles[0] for allele in alleles)

    heterozygotes = [is_heterozygous(genotype) for genotype in genotypes]

    # Frequency
    Ho = np.sum(heterozygotes) / len(genotypes)

    # Inbreeding
    return np.nan if He == 0 else (He - Ho) / He