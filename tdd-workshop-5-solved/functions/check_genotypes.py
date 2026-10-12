def check_genotypes(genotypes):
    """Check a list of genotypes and return it untouched if it is valid.

    genotypes: list of genotypes (e.g., ["AA", "Aa", "aa"])
    """

    # Check
    if isinstance(genotypes, (str, bytes)) or not hasattr(genotypes, "__len__"):
        raise TypeError("Input should be a list of genotypes")
    if len(genotypes) == 0:
        raise ValueError("Input vector is empty")

    # Convert to string if needed
    as_strings = [str(genotype) for genotype in genotypes]

    # Check ploidy
    n_alleles = len(as_strings[0])
    if any(len(genotype) != n_alleles for genotype in as_strings):
        raise ValueError("Not all genotypes have the same number of alleles")

    # Check for empty genotypes
    if n_alleles == 0:
        raise ValueError("Genotype cannot be empty")

    return genotypes
