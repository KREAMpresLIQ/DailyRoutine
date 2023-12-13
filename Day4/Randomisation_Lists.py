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
# Exercise Baker Roulette

names_string = input("Give me everybody's names, seperated by a comma.\n")
names = names_string.split(", ")

random_name_index = random.randint(0, len(names) - 1)
random_element = names[random_name_index]
print(f"{random_element} is going to buy the meal today")
