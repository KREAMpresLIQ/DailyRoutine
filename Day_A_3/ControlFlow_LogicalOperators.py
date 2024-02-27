print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill_roller = 0

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is you age? "))
    if age < 12:
        bill_roller = 5
        print("Child Ticket are $5.")
    elif 12 <= age <= 18:
        bill_roller = 7
        print("Youth Ticket are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill_roller = 12
        print("Adult Ticket are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill_roller = bill_roller + 3

    print(f"Your final bill is ${bill_roller}")

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

###################################
# Pizza Order

#  Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#  Don't change the code above

# Write your code below this line
price = 0

if size == "S":
    price = price + 15
elif size == "M":
    price = price + 20
elif size == "L":
    price = price + 25

if add_pepperoni == "Y":
    if size == "S":
        price = price + 2
    else:
        price = price + 3
if extra_cheese == "Y":
    price = price + 1

print(f"Your final bill is: ${price}")


#############################################
# Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

# Write your code below this line!

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
# int_score = int(love_score)

print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


###########################################
# Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('You\'re at a lake. What do you want to do? Type "swim" or "wait"\n').lower()
    if choice2 == "wait":
        choice3 = input('You\'re front of three doors. Which one do you open? Type "Red", "Blue", or "Yellow"')
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")