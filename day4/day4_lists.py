# Here I'll be learning about lists and data structures in Python. #

# Lists are a data structure in Python that can store multiple values. They are ordered and changeable. #

# You can create a list by using square brackets. #

# fruits = ["Apple", "Banana", "Cherry"]
# print(fruits)

# # You can access items in a list by referring to the index number. #

# print(fruits[1])

# # You can also use negative indexing to access items from the end of the list. #

# print(fruits[-1])

# We can also change items in the list by referring to the index number. #

# fruits[1] = "Grape"

# Append is used to add an item to the end of the list. #

# fruits.append("Orange")

# Extend is used to add multiple items to the end of the list. #

# fruits.extend(["Peach", "Pineapple"])

# Coding challenge - to randomly pick a name from a list of names to decide who pays a food bill. #

# #import random#
# import random

# #build a list of names#
# list_of_names = ["Jack", "Kelly", "Aaron", "Kimberly", "George", "Jasper"]

# #use the random module to select a random name - perhaps using randint to target the index at a random number between 0 and the length of the list of names#
# random_name = random.randint(0, len(list_of_names) - 1)

# #print the name of the person who will pay the bill#
# print(f"{list_of_names[random_name]} will pay the bill.")

# Index out of range error - this is because the random.randint function generates a random number between 0 and the length of the list of names. However, the length of the list of names is 6, so the random number generated will be between 0 and 5. This means that the index will be out of range if the random number generated is 6. To fix this, we need to subtract 1 from the length of the list of names. #

# Nested lists are lists that contain other lists. # 

# For example, a list of lists can be used to represent a 2D grid. #

fruits = ["Apple", "Banana", "Cherry"]
vegetables = ["Carrot", "Potato", "Spinach"]
animals = ["Dog", "Cat", "Rabbit"]

# Create a list of lists #
nested_list = [fruits, vegetables, animals]

# Access an item in the list of lists #
print(nested_list[1][2])

# This will print "Spinach" as it is the third item in the second list. #