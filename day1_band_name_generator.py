#This is a band name generator that takes a user city and pet name input then prints it to the console#

# print sends the string to the console #
# print("Hello world!")

# print("1. Mix 500g of flour, 10g Yeast and 300ml water in a bowl")
# print("2. Knead the dough for 10 minutes")
# print("3. Add 3g of salt")
# print("4. Leave to rise for 2 hours")
# print("5. Bake at 200 degrees c for 30 minutes")

# Using print but using \n to create a new line #
# print("1. Mix 500g of flour, 10g Yeast and 300ml water in a bowl\n2. Knead the dough for 10 minutes\n3. Add 3g of salt\n4. Leave to rise for 2 hours\n5. Bake at 200 degrees c for 30 minutes")

# We can also concatenate strings using the + operator #
# print("Hello" + " " + "Jack")

# We can also use the input function to get user input #
# input("What is your name? ")

# We can also store the input in a variable #
# name = input("What is your name? ")
# print("Hi there, " + name + "!")

# You can also do it all in one line #
# print("Hi there, " + input("What is your name? ") + "!")

# You can use several different functions to check the details of a string, for example, the length of a string #
# 
# print(len("Hello"))

# This is a band name generator exercise to highlight the use of input and print functions #
print("Welcome to the Band Name Generator")
city = input("What city did you grow up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name could be " + city + " " + pet)
