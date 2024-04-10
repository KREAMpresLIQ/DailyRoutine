# DEBUGGING

# # Describe Problem
# def my_function():
#     for i in range(1, 20): # 1 - 19 // for i in range(1,21)
#         # print(i)
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]  # 0 - 5
# dice_num = randint(1, 6)  # randint(0,5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if 1980 <= year <= 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# else:
#     print("You are Boomer!")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word per pages = {word_per_page}")
# print(f"total words = {total_words}")

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
