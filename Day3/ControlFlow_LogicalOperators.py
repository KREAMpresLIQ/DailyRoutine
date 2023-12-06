print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is you age? "))
    if age < 12:
        print("Please pay $5.")
    elif 12 <= age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you can't ride the rollercoaster!")


###### Even and Odd

#  Don't change the code below
number = int(input("Which number do you want to check? "))
#  Don't change the code above

#Write your code below this line

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