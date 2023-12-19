import random
import my_module

print(my_module.pi)

random_int = random.randint(100, 200)
print(random_int)

random_float = random.random()
print(random_float)

random_float_multi = random_float * 5
print(random_float_multi)

random_uniform = round(random.uniform(0, 5), 2)
print(random_uniform)

score = random.randint(1, 100)
print(f"Your score is {score}")

##################################
# Exercise Heads or Tails!

HeadOrTail = random.randint(0, 1)
print(HeadOrTail)

if HeadOrTail == 1:
    print("Heads")
else:
    print("Tails")

##################################

##################################
# List
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York",
                     "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
                     "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
print(states_of_america[49])
states_of_america.append("UnknownState")
states_of_america.extend(["Unknown", "State"])
print(states_of_america[-1])
states_of_america[1] = "Pencilvania"

print(states_of_america)


#####################################
# Exercise Banker Roulette

names_string = input("Give me everybody's names, seperated by a comma.\n")
names = names_string.split(", ")

random_name_index = random.randint(0, len(names) - 1)
random_element = names[random_name_index]
print(f"{random_element} is going to buy the meal today")


#####################################

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[1][1])

#####################################
# Treasure Map

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

# selected_row = map[row - 1]
# selected_row[column - 1] = "X"

map[row - 1][column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

#####################################
# Rock Paper Scissors Game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list_img = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(choice_list_img[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(choice_list_img[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a Draw!")
