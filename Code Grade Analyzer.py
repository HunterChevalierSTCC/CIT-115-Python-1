# Code Grade Analyzer

# Function to get a valid int input
def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

# Function to get a valid Y/N input
def get_valid_yn_input(prompt):
    while True:
        response = input(prompt).upper()
        if response in ['Y', 'N']:
            return response
        print("Enter Y or N to Drop the Lowest Grade.")

# Get student's name
s_name = input("Enter the student's name: ")

# Get test scores
i_scores = []
for i in range(4):
    score = get_valid_int_input("Enter test score " + str(i + 1) + ": ")
    if score < 0:
        print("Test scores must be greater than 0.")
        raise SystemExit

    i_scores.append(score)

# Ask if lowest grade should be dropped
s_drop_lowest = get_valid_yn_input("Drop the lowest grade? (Y/N): ")

# Calculate average
if s_drop_lowest == 'Y':
    # Find lowest score without using min() or list functions
    i_lowest = i_scores[0]
    for score in i_scores:
        if score < i_lowest:
            i_lowest = score

    f_sum = sum(i_scores) - i_lowest
    f_avg = f_sum / 3
else:
    f_avg = sum(i_scores) / 4

# Round the average to one decimal place
f_avg = round(f_avg, 1)

# Determine letter grade
if f_avg >= 97.0:
    s_grade = 'A+'
elif f_avg >= 94.0:
    s_grade = 'A'
elif f_avg >= 90.0:
    s_grade = 'A-'
elif f_avg >= 87.0:
    s_grade = 'B+'
elif f_avg >= 84.0:
    s_grade = 'B'
elif f_avg >= 80.0:
    s_grade = 'B-'
elif f_avg >= 77.0:
    s_grade = 'C+'
elif f_avg >= 74.0:
    s_grade = 'C'
elif f_avg >= 70.0:
    s_grade = 'C-'
elif f_avg >= 67.0:
    s_grade = 'D+'
elif f_avg >= 64.0:
    s_grade = 'D'
elif f_avg >= 60.0:
    s_grade = 'D-'
else:
    s_grade = 'F'

# Output results
print("Name: " + s_name)
print("Average: " + str(f_avg))
print("Letter Grade: " + s_grade)