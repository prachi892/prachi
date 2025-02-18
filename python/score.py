
score = int(input("Enter the score: "))

# Determine the grade using if-else statements
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 50 <= score < 60:
    grade = "E"
else:
    grade = "F"

# Print the grade
print(f"Your grade is: {grade}")
