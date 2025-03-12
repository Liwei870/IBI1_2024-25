# Commute time calculation part

# Define the time to walk to the bus stop (in minutes)
a = 15
# Define the time for the bus journey (in minutes), 1 hour and 15 minutes is 75 minutes
b = 75
# Calculate the total time for the bus - based commute (in minutes)
c = a + b

# Define the time for driving (in minutes), 1 hour and 30 minutes is 90 minutes
d = 90
# Define the time for walking from the car park (in minutes)
e = 5
# Calculate the total time for the car - based commute (in minutes)
f = d + e

# Compare the total times of the two commuting methods
if c < f:
    print("The bus - based commute is faster")
    # Record the result as a comment
    # The total time c for the bus - based commute is {} minutes, and the total time f for the car - based commute is {} minutes, so the bus - based commute is faster
elif c > f:
    print("The car - based commute is faster")
    # Record the result as a comment
    # The total time c for the bus - based commute is {} minutes, and the total time f for the car - based commute is {} minutes, so the car - based commute is faster
else:
    print("The two commuting methods take the same amount of time")
    # Record the result as a comment
    # The total time c for the bus - based commute is {} minutes, and the total time f for the car - based commute is {} minutes, so the two commuting methods take the same amount of time


# Boolean part

# Create boolean variable X and assign it to True
X = True
# Create boolean variable Y and assign it to False
Y = False

# Create variable W, representing the logical AND result of X and Y
W = X and Y

# Record the truth table of W as a comment
# Truth table:
# X   Y   W
# True True True
# True False False
# False True False
# False False False