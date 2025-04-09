#define a function to find the cut sites of a restriction enzyme in a DNA sequence
def find_cut_sites(dna_sequence, enzyme_sequence):
    valid_nucleotides = set('ACGT')
    if not all(nucleotide in valid_nucleotides for nucleotide in dna_sequence) or \
            not all(nucleotide in valid_nucleotides for nucleotide in enzyme_sequence):
        raise ValueError("The DNA sequence or enzyme recognition sequence must only contain ACGT nucleotides.")
    cut_sites = []
    for i in range(len(dna_sequence) - len(enzyme_sequence) + 1):
        if dna_sequence[i:i+len(enzyme_sequence)] == enzyme_sequence:
            cut_sites.append(i)
    return cut_sites   
#example usage
try:
    dna = "ACGTACGTACGT"
    enzyme = "ACGT"
    sites = find_cut_sites(dna, enzyme)
    print(f"Restriction sites: {sites}")
except ValueError as e:
    print(f"Error: {e}")                   
    