# TODO - Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("First statement")
    print("Second statement")
    print("Third statement")


greet()


# TODO - Function that allows for input

def greet_with_name(name, second_name):  # (Parameter)
    print(f"First statement {name}")
    print(f"Second statement {second_name}")


greet_with_name(" - Function Input {name}", " - Second Function Input {second_name}")  # (Argument)


# TODO - Functions with more than 1 input - Positional Argument

def greet_with(parameter1, parameter2):
    print(f"Hello {parameter1}")
    print(f"What is it like in {parameter2} ? ")


greet_with("KREAMpresLIQ", "Serbia")

# TODO - Keyword Arguments

# def greet_with_keyword(kparameter1 = "KREAMpresLIQ", kparameter2 = "Serbia"):
#     print(f"What is it like in {kparameter2} ? ")
#     print(f"Hello {kparameter1}")

greet_with(parameter2="Serbia", parameter1="KREAMpresLIQ")
