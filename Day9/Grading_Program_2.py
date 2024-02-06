student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Don't change the code above

# First *fork* your copy. Then copy-paste your code below this line
# Finally click "Run" to execute the tests

# TO DO-1: Create an empty dictionary called student_grades.
print(student_scores)
student_grades = {}

# TO DO-2: Write your code below to add the grades to student_grades.

for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# Don't change the code below
print(student_grades)
