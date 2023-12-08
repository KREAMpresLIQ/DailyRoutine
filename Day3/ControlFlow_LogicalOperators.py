print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is you age? "))
    if age < 12:
        print("Please pay $5.")
    elif 12 <= age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you can't ride the roller coaster!")

#####################################
# Even and Odd

#  Don't change the code below
number = int(input("Which number do you want to check? "))
#  Don't change the code above

# Write your code below this line

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number")

mod = number % 2
if mod >= 1:
    print("This is an odd number")
else:
    print("This is an even number")

# modulo_odd_1 = 3 % 2
# print(modulo_odd_1)
# modulo_odd_2 = 5 % 2
# print(modulo_odd_2)
# modulo_odd_3 = 7 % 2
# print(modulo_odd_3)
#
# module_even_1 = 4 % 2
# print(module_even_1)
# module_even_2 = 6 % 2
# print(module_even_2)
# module_even_3 = 8 % 2
# print(module_even_3)

###############################
# BMI 2.0

#  Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#  Don't change the code above

# Write your code below this line

BMI = (int(weight) / float(height) ** 2)
BMI_as_int = round(int(BMI))
print(BMI_as_int)

if BMI_as_int < 18.5:
    print(f"Your BMI is {BMI_as_int}, you are underweight")
elif 18.5 <= BMI_as_int < 25:
    print(f"Your BMI is {BMI_as_int}, you have a normal weight")
elif 25 <= BMI_as_int < 30:
    print(f"Your BMI is {BMI_as_int}, you are slightly overweight")
elif 30 <= BMI_as_int < 35:
    print(f"Your BMI is {BMI_as_int}, you are obese")
else:
    print(f"Your BMI is {BMI_as_int}, you are clinically obese")

#################################
# Leap Year

#  Don't change the code below
year = int(input("Which year do you want to check? "))
#  Don't change the code above

# Write your code below this line

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")
