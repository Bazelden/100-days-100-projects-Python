# Today we'll be building a tip calculator and in order to do this, we'll need to learn about data types and type conversion. # 

# Here are the primitive data types in Python: 
# 1. int (integer) or a whole number
# 2. float (floating point number) or a number with a decimal point
# 3. bool (boolean) or True or False
# 4. str (string) or a sequence of characters
# 5. list (list) or a collection of items
# 6. tuple (tuple) or a collection of items that cannot be changed
# 7. set (set) or a collection of unique items
# 8. dict (dictionary) or a collection of key-value pairs
# 9. NoneType (None) or a type representing the absence of a value

# Here is an example of pulling an element from a string using an index #
# "Hello"[0] # This will return the first character in the string "Hello" which is "H"
# print("Hello"[4]) # This will return the fifth character in the string "Hello" which is "o"

# Here is an example of converting a number to a string #
# str(123) # This will convert the number 123 to the string "123"
# print("123" + "456") # This will concatenate the two strings "123" and "456" to give "123456"

# PRO TIP: You can use negative indicies to pull elements from the end of a string #
# print("Hello"[-1]) # This will return the last character in the string "Hello" which is "o"

# Here is an example of converting a string to a number #
# int("123") # This will convert the string "123" to the number 123

# Here is an example of converting a number to a float #
# float(123) # This will convert the number 123 to the float 123.0

# Here is an example of converting a float to an int #
# int(123.0) # This will convert the float 123.0 to the int

# Here is an example of converting a number to a string #
# str(123) # This will convert the number 123 to the string "123"

# Here is an example of converting a string to a float #
# float("123.0") # This will convert the string "123.0" to the float 123.0

# Here is an example of converting a float to a string #
# str(123.0) # This will convert the float 123.0 to the string "123.0"

# This is a way we can check the data type of a value #
# print(type(123)) # This will return <class 'int'>
# print(type("123")) # This will return <class 'str'>
# print(type(123.0)) # This will return <class 'float'>
# print(type(True)) # This will return <class 'bool'>

# Here are some basic mathematical operations in Python #
# print(3 + 5) # This will print 8 - the result of the addition is an int
# print(7 - 4) # This will print 3 - the result of the subtraction is an int
# print(3 * 2) # This will print 6 - the result of the multiplication is an int
# print(6 / 3) # This will print 2.0 - the result of the division is a float 
# print(2 ** 3) # This will print 8 - 2 to the power of 3
# print(3 // 2) # This will print 1 - the integer division of 3 by 2 it will return the whole number part of the division (removes the decimal)
# print(3 % 2) # This will print 1 - the remainder of 3 divided by 2

# Here is an example of using the round function #
# print(round(8 / 3)) # This will print 3 - the result of 8 divided by 3 rounded to the nearest whole number
# print(round(8 / 3, 2)) # This will print 2.67 - the result of 8 divided by 3 rounded to 2 decimal places

# Here is an example of using the floor division operator #
# print(8 // 3) # This will print 2 - the result of 8 divided by 3 using integer division

# Pemdas - the order of operations in Python #
# Parentheses ()
# Exponents ** - this is the power operator 
# Multiplication *
# Division /
# Addition +
# Subtraction -

# Here is an example of using the order of operations #
# print(3 * 3 + 3 / 3 - 3) # This will print 7.0 - the result of 3 times 3 plus 3 divided by 3 minus 3

# Here is how to calculate if something is squared, for example a bmi #
# bmi = 22
# height = 1.75
# is_overweight = bmi / height ** 2

# Here's how to limit the number of decimal places in a float #
# print(f"{is_overweight:.2f}") # This will print 7.18 - the result of the bmi calculation rounded to 2 decimal places
# or we can round up or down to the nearest whole number #
# print(round(is_overweight)) # This will print 7 - the result of the bmi calculation rounded to the nearest
# print(round(is_overweight, 1)) # This will print 7.2 - the result of the bmi calculation rounded to 1 decimal place
# or we can floor the number to the nearest whole number #
# print(is_overweight // 1) # This will print 7.0 - the result of the bmi calculation floored to the nearest whole number

# Here is an example of using the f-string method to format a string #
# name = "Angela"
# print(f"Hello {name}") # This will print "Hello Angela"

# Here are some assignment operators in Python #
# x = 3 # This is the assignment operator
# x += 3 # This is the addition assignment operator
# x -= 3 # This is the subtraction assignment operator
# x *= 3 # This is the multiplication assignment operator
# x /= 3 # This is the division assignment operator
# x **= 3 # This is the exponent assignment operator
# x //= 3 # This is the floor division assignment operator
# x %= 3 # This is the modulus assignment operator

# Here is an example of using the assignment operator #
# x = 3

# Here is an example of using the addition assignment operator #
# x += 3 # This is the same as x = x + 3

# Here is an example of using the subtraction assignment operator #
# x -= 3 # This is the same as x = x - 3

# Here is an example of using the multiplication assignment operator #
# x *= 3 # This is the same as x = x * 3

# Here is an example of using the division assignment operator #
# x /= 3 # This is the same as x = x / 3

# Here is an example of using the exponent assignment operator #
# x **= 3 # This is the same as x = x ** 3

# Here is an example of using the floor division assignment operator #
# x //= 3 # This is the same as x = x // 3

# Here is an example of using the modulus assignment operator #
# x %= 3 # This is the same as x = x % 3

# Here is an example of using the tip calculator #
print("Welcome to the tip calculator!")
bill_total = float(input("What was the total of the bill in £? \n")) # This is the bill total
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? \n")) # This is the tip percentage
people = int(input("How many people are splitting the bill? \n")) # This is the number of people splitting the bill
tip = bill_total * tip_percentage / 100 # The reason we divide by 100 is to convert the percentage to a decimal number to get the tip amount
total = bill_total + tip # This is the total bill amount including the tip
split = total / people # This is the amount each person should pay
print(f"Each person should pay: £{round(split, 2)}") #here we use the f-string method to format the string and use round to round the number to 2 decimal places
# This is the end of the tip calculator





