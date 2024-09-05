# In day 4 I will be aiming to build a rock, paper scissors game whilst also learning about the random module, understanding the offset and appeding to a list, indexerrors and working with nested lists and finally building a rock, paper, scissors game. #

### Random Module ###
# The random module is a built-in module that allows you to generate random numbers. It can be used to simulate a random event. #

import random

# The random module has a function called randint that generates a random number between two integers. #

# The following code generates a random number between 1 and 6. #
# random_integer = random.randint(1, 6)
# print(random_integer)

# Modules are like toolkits that contain a set of functions that you can use in your code. #

# We can create our own modules by creating a new python file and importing it into our main file. #

# import my_module
# print(my_module.my_favorite_number)

# We can also do the same for random floating point numbers. #

# random_float = random.random() * 10
# print(random_float)

# random.uniform can also be used to generate random floating point numbers. #

# random_float = random.uniform(1, 10)
# print(random_float)

# We can also use randint to generate a random number which can be used as a true or false by using 1 or 0. #

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")
