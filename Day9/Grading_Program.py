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
    if student_scores[key] >= 91:
        student_scores[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_scores[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_scores[key] = "Acceptable"
    else:
        student_scores[key] = "Fail"
# print(student_scores)
student_grades = student_scores
# Don't change the code below
print(student_grades)
