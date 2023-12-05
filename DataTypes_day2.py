# Primitive Data Types

# String
print("Hello"[0])

print("123" + "456")

# Integer

print(123 + 456)

print(123_456_789)

# Float

print(3.14159)

# Boolean

print(False)
print(True)

#######################################################

# num_char = len(input("What is your name?"))
# print(type(num_char))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")

a = float(123)
print(type(a))  # <class 'float>

print(70 + float(100.5))  # 170.5
print(str(70) + str(100))  # 70100

######################################################

#  Don't change the code below
two_digit_number = input("Type a two digit number: ")
#  Don't change the code above

####################################
# Write your code below this line

first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])

print(first_num)
print(second_num)
# print(type(first_num))

add_digit_numbers = first_num + second_num
print(add_digit_numbers)

######################################################

# Mathematical

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
print(3 + 3 * 3 / 3 - 3)

######################################################

#  Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#  Don't change the code above

# Write your code below this line

# BMI = (int(weight) / (float(height) * float(height)))
# print(int(BMI))

BMI_solution_2 = (int(weight) / float(height) ** 2)
BMI_as_INTEGER = int(BMI_solution_2)
print(BMI_as_INTEGER)

######################################################

# Number Manipulating + F String

score = 0
height = 1.8
isWinning = True
# f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#  Don't change the code below
age = input("What is your current age?")
#  Don't change the code above

# Write your code below this line
age_as_int = int(age)
age_death = 90
age_calculate = age_death - age_as_int
age_days = round(age_calculate * 365)
age_weeks = round(age_calculate * 52)
age_months = round(age_calculate * 12)
print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")


######################################################

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?: "))
people = int(input("How many people to split the bill?: "))
tip_percent = tip / 100
print(tip_percent)
total_tip = bill * tip_percent
print(total_tip)
total_pay = bill + total_tip
print(total_pay)
per_person_pay = total_pay / people
print(per_person_pay)
final_pay = round(per_person_pay, 2)
print(f"Each person should pay: ${final_pay}")


