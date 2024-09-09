# Here I'll be doing a coding exercise involving a high score checker, taking in a list of scores and outputting the highest score. #

# High Score Checker #

# Given a list of scores, this program will output the highest score. #

# List of scores #

student_scores = [78, 65, 89, 86, 55, 91, 64, 89, 81, 90]

# Highest score #
# We need a variable to hold the values and then iterate through the student scores that updates the value of the variable if the next score is higher than the current score and if not, the value of the variable remains the same. The end result should be 91. #

# Initialize the highest score to 0 #
highest_score = 0

# Iterate through the student scores #
for score in student_scores:
    # Check if the score is greater than the highest score #
    if score > highest_score:
        # If the score is greater than the highest score, update the highest score #
        highest_score = score
#print the highest score using an f-string #
print(f"The highest score in the class is: {highest_score}")

# Output: The highest score in the class is: 91

# This can also be done using the max() function. #

max_score = max(student_scores)
print(f"The highest score in the class is: {max_score}")