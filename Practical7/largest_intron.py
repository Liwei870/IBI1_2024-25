#import seq
# use string to find the largest intron
import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
matches = re.finditer(r'GT([ATGC]{6,}?)AG', seq)  # use regex to find the largest intron
max_length = 0
for match in matches:
    intron_length = len(match.group(0)) 
    if intron_length > max_length:
        max_length = intron_length
    print(f"The largest intron is: {max_length+2} bp (including GT/AG)")
    

