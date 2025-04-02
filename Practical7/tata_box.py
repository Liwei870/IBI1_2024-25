#read the file Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa
#identify sequences which contain at least one TATA box sequence
# and write them to a new file
import re
pattern = re.compile(r'TATA[AT]A[AT]')
SEQUENCE_LINE_LENGTH = 80
with open("E:\IBI1\IBI1_2024-25\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa") as infile, \
     open("E:\IBI1\IBI1_2024-25\IBI1_2024-25\Practical7\ tata_genes.fa", "w") as outfile:  
    gene_name = ""
    sequence = []
    def write_sequence(header, seq):
       # Write the sequence to the output file in 80-character lines
        # with the header line
        outfile.write(f'>{header}\n')
        for i in range(0, len(seq), SEQUENCE_LINE_LENGTH):
            outfile.write(seq[i:i+SEQUENCE_LINE_LENGTH] + '\n')
    
    for line in infile:
        if line.startswith('>'):
       #check if the previous sequence contains TATA box
            if sequence and pattern.search(''.join(sequence)):
                write_sequence(gene_name, ''.join(sequence))
            
            # Reset for the next gene
            gene_name = line.split('gene:')[1].split()[0]
            sequence = []
        else:
            sequence.append(line.strip())
    
    # Check the last sequence after the loop
    if sequence and pattern.search(''.join(sequence)):
        write_sequence(gene_name, ''.join(sequence))