from collections import Counter

import numpy as np


def inbreeding_coefficient(genotypes):
    """Calculate the inbreeding coefficient.

    genotypes: list of genotypes (e.g., ["AA", "Aa", "aa"])
    """

    # Check
    if isinstance(genotypes, (str, bytes)) or not hasattr(genotypes, "__len__"):
        raise TypeError("Input should be a list of genotypes")
    if len(genotypes) == 0:
        raise ValueError("Input vector is empty")

    # Convert to string if needed
    genotypes = [str(genotype) for genotype in genotypes]

    # Check ploidy
    n_alleles = len(genotypes[0])
    if any(len(genotype) != n_alleles for genotype in genotypes):
        raise ValueError("Not all genotypes have the same number of alleles")

    # Check for empty genotypes
    if n_alleles == 0:
        raise ValueError("Genotype cannot be empty") # NEW CHECK ADDED

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