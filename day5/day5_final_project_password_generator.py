# # For the final project of day 5 we will be taking user input to generate a password. The password will be a combination of letters, numbers and symbols. The user will be able to choose the length of the password. #

# # Import the random module to shuffle the letters, numbers and symbols
# import random

# # Create a list of letters, numbers and symbols
# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# # Take users input for length of password using prompts for each list and store them as variables
# print("Welcome to Jacks Python Password Generator!")

# pw_letters = int(input("How many letters would you like in your password?\n"))
# pw_numbers = int(input("How many numbers would you like in your password?\n"))
# pw_symbols = int(input("How many symbols would you like in your password?\n"))

# # Create an empty list to store the password

# password_list = []

# # Use a for loop to iterate through the range of the length of the password and append the letters, numbers and symbols to the password list
# for i in range(pw_letters):
#     password_list.append(random.choice(letters))

# for i in range(pw_numbers):
#     password_list.append(random.choice(numbers))

# for i in range(pw_symbols):
#     password_list.append(random.choice(symbols))

# # randomly reorder the password list using the shuffle method
# random.shuffle(password_list)

# # Create an empty string to store the password
# password = ""

# # Use a for loop to iterate through the password list and append the values to the password string
# for i in password_list:
#     password += i
#     password.join(i)

# # Print the password
# print(f"Your password is: {password}")

# Going to try and build the password generator taking one input from the user #

# import random

# password_pieces = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "#", "$", "%", "&", "(", ")", "*", "+"]
# password_list = []
# password = ""

# print("Welcome to Jacks Python Password Generator!")
# pw_length = int(input("How many characters would you like in your password?\n"))

# for i in range(pw_length):
#     password += random.choice(password_pieces)
#     password_list.append(password)
#     random.shuffle(password_list)

# for i in password_list:
#     password.join(i)

# print(f"Your password is: {password}")



