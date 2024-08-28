# In day 3 I will be working to build a text based choose your own adventure game and will be learning about control flow and conditional operators in python #

# If and else statements can be used to add conditional logic to your code. If the condition is true, the code block under the if statement will run. If the condition is false, the code block under the else statement will run. # 

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you aren't tall enough to ride the rollercoaster! :(.")

# In the above code, the user is asked to input their height in cm. If the height is greater than or equal to 120, the user can ride the rollercoaster. If the height is less than 120, the user is not tall enough to ride the rollercoaster. #

# Comparison operators can be used to compare two values. The result of the comparison is a boolean value. The comparison operators are: >, <, >=, <=, ==, !=. #

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?\n "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you aren't tall enough to ride the rollercoaster! :(.")

# Below I'll cover what I've learned about the modular operator. The modular operator is represented by the % symbol. It is used to find the remainder of a division operation. #

# print(6 % 2) # 0
# print(5 % 2) # 1
# print(8 % 3) # 2

# The modular operator can be used to determine if a number is even or odd. If a number is divided by 2 and the remainder is 0, the number is even. If the remainder is 1, the number is odd. #

# Here is an example of how to use the modular operator to determine if a number is even or odd. #

# number_to_check = int(input("What is the number you want to check? \n"))
# print(number_to_check % 2)
# if number_to_check % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# Nested if statements can be used to add more conditional logic to your code. Nested if statements are if statements that are inside of other if statements. #

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?\n "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you aren't tall enough to ride the rollercoaster! :(.")

# We can use subsequent if statements to add more conditional logic to our code. #

# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm?\n "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?\n "))
#     if age < 12:
#         print("Child tickets are £5.")
#         bill += 5
#     elif age <= 18:
#         print("Youth tickets are £8.")
#         bill += 8
#     else:
#         print("Adult tickets are £12.")
#         bill += 12

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         print("That will be an extra £3.")
#         bill += 3

#     print(f"Your final bill is £{bill}.")

# else:
#     print("Sorry, you aren't tall enough to ride the rollercoaster! :(.")

# In the above code, the user is asked if they want a photo taken. If the user wants a photo taken, the bill is increased by £3. The final bill is printed to the console. #

# Pizza challenge - create a python pizza delivery programme that calculates the total cost of a pizza order. #

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L. ")
# pepperoni = input("Do you want pepperoni? Y or N. ")
# extra_cheese = input("Do you want extra cheese? Y or N. ")
# pineappe = input("Do you want pineapple? Y or N. ")

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# if pineappe == "Y":
#     print("I just saw you like pineapple on pizza - please leave.")
# else:
#     print(f"Thank you for your order - the total comes to £{bill}.")

# Logical operators can be used to combine multiple conditions in an if statement. The logical operators are: and, or, not. #

# and. The and operator returns True if both conditions are true. #
# or. The or operator returns True if at least one condition is true. #
# not. The not operator returns the opposite of the condition. #

# Here I will be crating a choose your own adventure book as a final exercise for today. #

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroads. Where do you want to go? Type 'left' or 'right'. ")
if choice1 == "right":
    print("You choose right and accidently fall into a hole. Game over.")
else:
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across. ")
    if choice2 == "swim":
        print("You try to swim over and get dragged under water to your doom by a water monster. Game over.")
    else:
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if choice3 == "red":
            print("You open the door and fire engulfs you! Game over.")
        elif choice3 == "yellow":
            print("You open the door and gold pours out! You win!")
        else:
            print("You open the door and are swept back into the lake where a sea monster drags you to a watery grave... Game over.")