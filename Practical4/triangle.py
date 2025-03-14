# Pseucode: Calculate and display the first ten values of the triangular number sequence
# Initialize a variable 'n' to represent the number of dots on each side of the triangle, starting with 1
n = 1
# Initialize a counter 'count' to record the number of triangular numbers that have been calculated, starting with 0
count = 0
# Execute the loop while the number of calculated triangular numbers is less than 10
while count < 10:
    triangular_number = n*(n+1)// 2
    # Print the 'n'-th triangular number
    print(f"The {n}-th triangular number is: {triangular_number}")
    # Increment 'n' by 1 to prepare for calculating the next triangular number
    n += 1
    # Increment the counter 'count' by 1 to record that one more triangular number has been calculated
    count += 1
 
