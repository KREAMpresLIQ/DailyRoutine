## Printing to the console

## Instructions

Write a program in start.py that print the same notes from the previous lesson using  what you have
learn about the Python print function.

**Warning:** The output in your program should match the example output shown below exactly, character for character, even spaces and symbols should be indetical,
otherwise the test won't pass.

# Example Output

After you have written your code, you should run your program and it should print the following:
```
Day 1 - Python Print Function
```

```
The function is declared like this:
```

```
print('what to print')
```

**e.g.** When you hit **run**, this is what should happen: 

![Alt Text](https://replit.com/cdn-cgi/image/quality=80,metadata=copyright,format=auto/https://raw.githubusercontent.com/angelabauer/100-days-gifs/main/1.1.%20print.gif)


## Test Your Code

---

## Debugging

# Instructions

Look at the code in the vode editor on the left. There are errors in all of the lines of code.
Fix the code so that it runs without errors.

**Warning:** The output in your program should match the example output **shown below** exactly, character for character, even spaces and symbols should be identical, otherwise the tests won't pass.

# Example Output

When you run your program, it should print the following:

```
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + " world")
New lines can be created with a backslash and n.
```

e.g. When you hit **run**, there should be no error and this is what should happen:

# Test your Code

---

## Inputs

---

# Instuctions 

---

Write a program that print the number of characters in a user's name.
You might need to Google for a function that calculates the length of a string

e.g.

https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow

**Warning.** Your program should work for different inputs. e.g. any name that you input.

# Example Input

---

```
Norbert
```

# Example Output

---

```
7
```

e.g. When you hit **run**, this is what should happen:


## Hint

---

1. You can put functions inside other functions.
2. Don't try to print anything other than the length

## Test Your Code

---

Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-1-3-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.


# Variables

---

## Instructions

---

Write a program that switches the values stored in the variables **a** and **b**.

**Warning.** Do not change the code on lines **51-54** and **65-67**. Your program should work for different inputs. e.g. any value of **a** and **b**.

## Example Input

---

```
a: 3
```
```
b: 5
```

## Example Output

---

```
a: 5
```
```
b: 3
```
e.g. When you hit run, this is what should happen:

```

```
## Hint

---

1. You should not have to type any numbers in your code.
2. You might need to make some more variables.

## Test Your Code

---

# Data Types

---

## Instructions

---

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8 <br>
***Warning.*** Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

## Example Input

---

```
39
```

## Example Output

---

3 + 9 = 12

```
12
```

e.g. When you hit **run**, this is what should happen:
```
```

## Hint

---

1.  Try to find out the data type of two_digit_number.
2.  Think about what you learnt about subscripting.
3.  Think about tpye conversion.

---

# BMI Calculator

---

## Instructions

---

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weight the same amount, the short person is usually more overweight. <br>
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
```

```
**Warning** you should convert the result to a whole number.

## Example Input

---

```
weight = 80
```
```
height = 1.75
```

## Example Output

---

80 ÷ (1.75 x 1.75) = 26.122448979591837

```
26
```

e.g. When you hit **run**, this is what should happen:

```

```

## Hint

---

1.  Check the data type of the inputs.
2. Try to use the exponent operator in your code.
3. Remember PEMDAS
4. Remember to convert your result to a whole number (int).

--- 

# Solution

---

https://repl.it/@appbrewery/day-2-2-solution

---

# Your Life in Weeks

---

## Instructions

---

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

<blockquote>
You have x days, y weeks, and z months left.
</blockquote>

Where x, y and z are replaced with the actual calculated numbers.

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

## Example Input

---

```
56
```

## Example Output

---

```
You have 12410 days, 1768 weeks, and 408 months left.
```

e.g. When you hit **run**, this is what should happen:

```

```

# Hint

---

1.  There are 365 days in a year, 52 weeks in a year and 12 month in a year.
2.  Remember to round the results before printing.

# Solution

https://replit.com/@appbrewery/day-2-3-solution#main.py

---

# Tip Calculator

---

## Instructions

---

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

This everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

## Example Input

---

```
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
```

## Example Output

---

```
Each person should pay: $19.93
```

## Hint

---

1.  <a node="[object Object]" href="https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal" target="_blank" rel="nofollow"> How to round a number to 2 decimal places in python</a>
2.  <a node="[object Object]" href="https://www.adamsmith.haus/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python" target="_blank" rel="nofollow"> How to limit a float to two decimal places in Python</a>

## Solution

---

https://replit.com/@appbrewery/tip-calculator-end#main.py

---

# Logical Operators and Control Flow
# Odd or Even

---

## Instructions

---

Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is **even** because 86 ÷ 2 = 43

43 does not have any decimal places. Therefor the division is clean.

e.g. 59 is **odd** because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefor there is a remainder of 0.5, so the division ios not clean

The **modulo** is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.

```
6 % 2 = 0
```
5 ÷ 2 = 2 x 2 + 1, remainder is 1.
```
5 % 2 = 1
```
14 ÷ 4 = 3 x 4 + 2, remainder is 2.
```
14 % 4 = 2
```

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

## Example Input 1

---

```
43
```
## Example Output 1

---

```
This is an odd number.
```

## Example Input 2

---

```
94
```

## Example Output 2

---

```
This is an even number.
```

e.g. When you hit **run**, this is what should happen:

```

```

## Hint

---

1.  All even numbers can be divided by 2 with 0 remainder.
2.  Try some using the modulo with some odd numbers e.g.

```
3 % 2
```
```
5 % 2
```
```
7 % 2
```
Then try using the modulo with some even numbers e.g.

```
4 % 2
```
```
6 % 2
```
```
8 % 2
```
See what's in common each time.

## Test Your Code

---

Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-1-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

## Solution 

---

https://repl.it/@appbrewery/day-3-1-solution