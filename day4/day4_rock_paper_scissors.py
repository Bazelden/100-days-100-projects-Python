# To finish the day - we'll be building a rock, paper, scissors game. #

import random

# Rock, Paper, Scissors Game #

# Create a list of choices #
choices = ["Rock", "Paper", "Scissors"]

# Ask the user to make a choice #
user_choice = input("Enter Rock, Paper, or Scissors: ")

# Generate a random choice for the computer using random and randint - setting the range to 0 and 2 to ensure the computer can only choose from the list of choices #
computer_choice = random.randint(0, 2)

# Print the choices using f-strings #
print(f"User choice: {user_choice}")

# if user_choice not in choices:
#     print("Invalid choice - Please choose either Rock, Paper, or Scissors.")
#     user_choice = input("Enter Rock, Paper, or Scissors: ")
# This will print an error message if the user choice is not in the list of choices. - but still runs the rest of the code...learn how to break out of the code if this is the case. #
# This solves the issue of the user choice not being in the list of choices for one instance, but if the user choice is not in the list of choices for a second time, the code will break. #
# I need to find a way to loop this back to the input line if the user choice is not in the list of choices. #
# Can I wrap it in a while loop? #
# Below code seems to work - keeping comments for revision purposes. #

while user_choice not in choices:
    print("Invalid choice - Please choose either Rock, Paper, or Scissors.")
    user_choice = input("Enter Rock, Paper, or Scissors: ")
# This will loop the code back to the input line if the user choice is not in the list of choices. #

print(f"Computer choice: {choices[computer_choice]}")

# Determine the winner using if statements and take into considering if the results are the same, it's a draw #

if user_choice == choices[computer_choice]:
    print("It's a draw!")
elif user_choice == "Rock" and choices[computer_choice] == "Scissors":
    print("You win!")
elif user_choice == "Paper" and choices[computer_choice] == "Rock":
    print("You win!")
elif user_choice == "Scissors" and choices[computer_choice] == "Paper":
    print("You win!")
else:
    print("You lose!")


# One thing to note - if user choice is anything other than the 3 in the list then you will automatically lose - try and find a way to catch this and print an error message to the user. #


# This is the end of day 4 - I've learnt about the random module, offset, appending to a list, indexerrors, working with nested lists and building a rock, paper, scissors game. #