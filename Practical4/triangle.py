# Purpose: Calculate and display the first ten values of the triangular number sequence
# Initialize a variable 'n' to represent the number of dots on each side of the triangle, starting with 1
n = 1
# Initialize a counter 'count' to record the number of triangular numbers that have been calculated, starting with 0
count = 0
# Execute the loop while the number of calculated triangular numbers is less than 10
while count < 10:
    # Initialize a variable'sum_value' to accumulate the numbers from 1 to 'n', starting with 0
    sum_value = 0
    # Initialize a variable 'i' for loop counting, starting with 1
    i = 1
    # Execute the loop and accumulate the numbers from 1 to 'n' while 'i' is less than or equal to 'n'
    while i <= n:
        sum_value += i
        i += 1
    # Print the 'n'-th triangular number
    print(f"The {n}-th triangular number is: {sum_value}")
    # Increment 'n' by 1 to prepare for calculating the next triangular number
    n += 1
    # Increment the counter 'count' by 1 to record that one more triangular number has been calculated
    count += 1
 
