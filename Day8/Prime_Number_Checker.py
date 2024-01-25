# Write your code below this line

def prime_checker(number):
    if number == 1:
        print(f"{number}, is not a prime number")
    elif number > 1:
        for i in range(2, number):
            if (number % i ) == 0:
                print(number, "is not a prime number")
                print(i, "times", number//i,"is", number)
                break
        else:
            print(number,"is a prime number")
    else:
        print(number,"is not a prime number")

# Write your code above this line

# Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)

