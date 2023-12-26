fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits)


#############################
# Student heights
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

sum_heights = 0
for heights in student_heights:
    sum_heights += heights
print(f"Student heights sum: {sum_heights}")

sum_students = 0
for students in student_heights:
    sum_students += 1
print(f"Student numbers sum: {sum_students}")

average_heights = round(sum_heights / sum_students)
print(f"Students average heights: {average_heights}")


############################
# Highest Score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# highest_score = len(student_scores) - 1
# for score in range(highest_score):
#     if student_scores[score] > student_scores[score + 1]:
#         student_scores[score], student_scores[score + 1] = student_scores[score + 1], student_scores[score]
# print(f'The highest score is: {student_scores[-1]}')

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")




