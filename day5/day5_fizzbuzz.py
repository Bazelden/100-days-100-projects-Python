# Here I will be trying to solve a fizzbuzz challenge that will take a range from 1-100 and if a number is divisible by 3, print fizz - divisible by 5, print buzz - divisible by 3 and 5, print fizzbuzz # 

# Set the range between 1-101 so the value 100 is included # 
fizzbuzz_range = range(1, 101)

# Iterate through the range using a for loop # 
for i in fizzbuzz_range:
    # Check if the number is divisible by 3 and 5 #
    if i % 3 == 0 and i % 5 == 0:
        # If the number is divisible by 3 and 5, print fizzbuzz #
        print("fizzbuzz")
    # Check if the number is divisible by 3 #
    elif i % 3 == 0:
        # If the number is divisible by 3, print fizz #
        print("fizz")
    # Check if the number is divisible by 5 #
    elif i % 5 == 0:
        # If the number is divisible by 5, print buzz #
        print("buzz")
    # If the number is not divisible by 3 or 5, print the number #
    else:
        print(i)


