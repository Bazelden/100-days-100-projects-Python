# In this file, we will learn about for loops and range function in Python #

# Range function in python #
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. #
# Syntax: range(start, stop, step) #
# start: Optional. An integer number specifying at which position to start. Default is 0 #
# stop: Required. An integer number specifying at which position to stop (not included). #
# step: Optional. An integer number specifying the incrementation. Default is 1 #

# Example 1: Using the range function  and for loop to print numbers from 0 to 5 #
# range = range(6)
# for i in range:
#     print(i)
# Output: 0 1 2 3 4 5

# Example 2: Using the range function and for loop to print numbers from 2 to 6 #
# range = range(2, 7)
# for i in range:
#     print(i)
# # Output: 2 3 4 5 6

# Example 3: Using the range function and for loop to print numbers from 2 to 30 in increments of 3 #
# range = range(2, 31, 3)
# for i in range:
#     print(i)
# # Output: 2 5 8 11 14 17 20 23 26

# Next we will try to solve the Gauss problem using the range function and for loop #

# # Gauss problem #
# # Set the range, starting from 1 to 101 as this will use the valuies 1-100
# gauss_range = range(1, 101)
# # Create a variable to store the total value
# gauss_sum = 0
# # Iterate through the range
# for i in gauss_range:
#     # For each index, the value should be added to the variable
#     gauss_sum += i
# # Print the total amount of the variable
# print(gauss_sum)

