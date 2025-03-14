# What does this piece of code do?
# Answer:the code is used to find the number of loop iterations it takes to find two equal random numbers in the range of 1 - 6.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
# when the first random is not equal to the second random number, the loop will continue and the process will record how many times it loop
while progress>=0:
	progress+=1
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n:
		print(progress)
		break
# My opinion: may be this code is to find two equal random number and record how many times to find two equal random numbers in the range of 1 - 6
