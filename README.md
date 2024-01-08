# Printing to the console

## Instructions

Write a program in start.py that print the same notes from the previous lesson using what you have
learn about the Python print function.

**Warning:** The output in your program should match the example output shown below exactly, character for character,
even spaces and symbols should be identical,
otherwise the test won't pass.

# Example Output

After you have written your code, you should run your program, and it should print the following:

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

Look at the code in the code editor on the left. There are errors in of the lines of code.
Fix the code so that it runs without errors.

**Warning:** The output in your program should match the example output **shown below** exactly, character for
character, even spaces and symbols should be identical, otherwise the tests won't pass.

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

# Instructions

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

**Warning.** Do not change the code on lines **51-54** and **65-67**. Your program should work for different inputs.
e.g. any value of **a** and **b**.

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

Write a program that adds the digits in a two-digit number. e.g. if the input was 35, then the output should be 3 + 5 =
8 <br>
***Warning.*** Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit
number.

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

1. Try to find out the data type of two_digit_number.
2. Think about what you learnt about subscripting.
3. Think about type conversion.

---

# BMI Calculator

---

## Instructions

---

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some weight taking into account their height. e.g. If a tall person and a short person both
weight the same amount, the short person is usually more overweight. <br>
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

1. Check the data type of the inputs.
2. Try to use the exponent operator in your code.
3. Remember #PEMDAS
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

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90
years old.

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

1. There are 365 days in a year, 52 weeks in a year and 12 month in a year.
2. Remember to round the results before printing.

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

1. All even numbers can be divided by 2 with 0 remainder.
2. Try some using the modulo with some odd numbers e.g.

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

---

# BMI Calculator 2.0

---

## Instructions

---

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

<li>Under 18.5 they are underweight</li>
<li>Over 18.5 but below 25 they have a normal weight</li>
<li>Over 25 but below 30 they are slightly overweight</li>
<li>Over 30 but below 35 they are obese</li>
<li>Above 35 they are clinically obese.</li>

```
```

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

```
```

**Warning** you should **round** the result to the nearest whole number. The interpretation message needs to include the
words in bold from the interpretations above. e.g. **underweight, normal weight, obese, clinically obese.**

## Example Input

---

```
weight = 85
```

```
height = 1.75
```

## Example Output

---

85 ÷ (1.75 x 1.75) = 27.755102040816325

```
Your BMI is 28, you are slightly overweight.
```

e.g. When you hit **run**, this is what should happen:

```
```

The testing code will check for print output that is formatted like one of the lines below:

```
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
```

## Hint

---

1. Try to use the **exponent** operator in your code.
2. Remember to **round** your result to the nearest whole number.
3. Make sure you include the words in **bold** from the interpretations.

## Test Your Code

---
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-2-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

## Solution

---

https://repl.it/@appbrewery/day-3-2-solution

---

# Leap Year

---

## Instructions

---

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366,
with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

<blockquote class="text-orange">
<style>.text-orange{color:darkorange;}</style>
on every year that is evenly divisible by 4 except every year that is evenly divisible
by 100 unless the year is also evenly divisible by 400
</blockquote>

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

## Example Input 1

---

```
2400
```

## Example Output 1

---

```
Leap year.
```

## Example Input 2

---

```
1989
```

## Example Output 2

---

```
Not leap year.
```

e.g. When you hit **run**, this is what should happen:

```

```

## Hint

---

1. Try to visualize the rules by creating a flow chart on www.drag.io
2. If you really get stuck, you can see the flow chart I created:

https://bit.ly/36BjS2D

## Test Your Code

---

Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-3-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

## Solution

---

https://repl.it/@appbrewery/day-3-3-solution

---

# Pizza Order

---

## Instructions

---

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: +$1
```

## Example Input

---

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

## Example Output

---

```
Your final bill is: $28.
```

e.g. When you hit **run**, this is what should happen:

```

```

## Hint

---

1. Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code
   while having the same functionality.

## Test Your Code

---

Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-4-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

## Solution

---

https://repl.it/@appbrewery/day-3-4-solution

---

# Love Calculator

---

## Instructions

---

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

<blockquote>

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the
number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2-digit number.

</blockquote>

**For Love Scores less than 10** or **greater than 90, the message should be:**

```
"Your score is **x**, you go together like coke and mentos.
```

**For Love Scores between 40** and **50, the message should be:**

```
"Your score is **y**, you are alright together."
```

**Otherwise, the message will just be their score. e.g.:**

```
"Your score is **z**
```

e.g.

```
name1 = "Jack Bauer"
name2 = "Ana Manson"
```

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

## Example Input 1

---

```
name1 = "Kanye West"
```

```
name1 = "Kim Kardashian"
```

## Example Output 1

---

```
Your score is 42, you are alright together.
```

## Example Input 2

---

```
name1 = "Brad Pitt"
```

```
name1 = "Jennifer Aniston"
```

## Example Output 2

---

```
Your score is 73
```

The testing code will check for print output that is formatted like one of the lines below:

```
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
```

## Score Comparison

---

Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

<table><thead><tr><th>Name 1</th><th>Name 2</th><th>Score</th></tr></thead><tbody><tr><td>Catherine Zeta-Jones</td><td>Michael Douglas</td><td>99</td></tr><tr><td>Brad Pitt</td><td>Jennifer Aniston</td><td>73</td></tr><tr><td>Prince William</td><td>Kate Middleton</td><td>67</td></tr><tr><td>Angela Yu</td><td>Jack Bauer</td><td>53</td></tr><tr><td>Kanye West</td><td>Kim Kardashian</td><td>42</td></tr><tr><td>Beyonce</td><td>Jay-Z</td><td>23</td></tr><tr><td>John Lennon</td><td>Yoko Ono</td><td>18</td></tr></tbody></table>

## Hint

---

1. The **lower()** function changes all the letters in a string to lowercase.
https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
2. The **count()** function will give you the number of times a letter occurs in a string.
https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

## Test Your Code

---

Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-5-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

## Solution 

---

https://repl.it/@appbrewery/day-3-5-solution

---

# Treasure Island

---

## Instructions

---

Make your own "Choose Your Own Adventure" game. Use conditionals such as **if, else,** and **elif** statements to lay out the logic and the story's path in your program.

<a node="[object Object]" href="https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload" target="_blank" rel="nofollow">To write your code according to my story, you can use this flow chart from draw.io to help you.</a>

However, I think the fun part is writing your own story.

That said if you'd like to continue with my example, feel free to use the text snippets below...

**Text Snippets from my example**

<ul>
<li>'You're at a crossroad. Where do you want to go? Type "left" or "right"'</li>
<li>'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'</li>
<li>"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"</li>
<li>"It's a room full of fire. Game Over."</li>
<li>"You found the treasure! You Win!"</li>
<li>"You enter a room of beasts. Game Over."</li>
<li>"You chose a door that doesn't exist. Game Over."</li>
<li>"You get attacked by an angry trout. Game Over."</li>
<li>"You fell into a hole. Game Over."</li>
</ul>

## Escaping Characters

---

If you want to use multiple sets of quotes inside a single string, you might have to "escape" some of them using the backslash \. You can see this in my first sentence: 'You're at a crossroad...'. <a node="[object Object]" href="https://www.w3schools.com/python/gloss_python_escape_characters.asp">More on escaping characters here.</a>

## Extensions

---

Have a think about how you might write your program to make a player's answers less case-sensitive. In other words, your code should work regardless of whether your user answers "left" or "Left".

<a node="[object Object]" href="https://ascii.co.uk/art">You can also add your own ASCII art.</a>
Just remember to add three single quotes **```** at the start and at the end of your artwork to turn it into a multi-line string.

---

# Heads or Tails

---

## Instructions

---

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g. 1 means Heads, 0 means Tails.

## Example Output

---

```
Heads
```

or

```
Tails
```

## Solution

---

https://replit.com/@appbrewery/day-4-1-solution

---

# Who's Paying

---

## Instructions

---

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

**Important**: You are not allowed to use the ```choice()``` function.

**Line 8** splits the string names ```names_string``` into individual names and puts them inside a **List** called ```names```. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name.

## Example Input

---

```
Angela, Ben, Jenny, Michael, Chloe
```

Note: notice that there is a space between the comma and the next name.

## Example Output

---

```
Michael is going to buy the meal today!
```

## Hint

---

1. You might need to help of the ```len()``` function.
https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list-length-of-a-list-in-python
2. Remember that Lists start at index **0**!

## Solution

---

https://replit.com/@appbrewery/day-4-2-solution

---

# Treasure Map

---

## Instructions

You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called ```map```

This ```map``` contains a nested list. When ```map``` is printed this is what the nested list looks like:

```
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
```

In the starting code, we have used new lines ```(\n)``` to format the three rows into a square, like this:

```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```

this is to try and simulate the coordinates on a real map.

<img node="[object Object]" src="https://replit.com/cdn-cgi/image/quality=80,metadata=copyright,format=auto/https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1440,f_auto/Co-ordinates_oggjzg.jpg" alt="" class="css-17vj7l">

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit for the input will specify the column (the position on the horizontal axis). The second digit in the input will specify the row number (the position on the vertical axis).

First your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

## Example Input 1

---

column 2, row 3 would be entered as:

```
23
```

## Example Output 1

---

```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
```

## Example Input 2

---

column 3, row 1 would be entered as:

```
31
```

## Example Output 2

---

```
['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```

e.g. When you hit **run**, this is what should happen:

```

```

## Hint 

---

1. Remember that Lists start at index 0!
2. ```map``` is just a variable that contains a nested list. It's not related to the map function in Python.

## Solution

---

https://repl.it/@appbrewery/day-4-3-solution

---

# Rock Paper Scissors

---

## Instructions

---

Make a rock, paper, scissors game.

Inside the ```main.py``` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable:
```rock```, ```paper```, and ```scissors```. This will make it easy to print them out to the console.

Start the game by asking the player: 

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:
<li>How you will store the user's input.</li>
<li>How you will generate a random choice for the computer.</li>
<li>How you will compare the user's and the computer's choice to determine the winner (or a draw)</li>
<li>And also how you will give feedback to the player.</li>

You can find the "official" rules of the game on <a node="[object Object]" href="https://wrpsa.com/the-official-rules-of-rock-paper-scissors/" target="_blank" rel="nofollow"> the World Rock Paper Scissors Association website.</a>

## Solution

---

https://replit.com/@appbrewery/rock-paper-scissors-end

---

# Loops

---

# Average Height

---

## Instructions

---

You are going to write a program that calculates the average student height from a List of heights.

e.g. ```student_heights = [180, 124, 165, 173, 189, 169, 146]```

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are total of **7** heights in ```student_heights```

1146 % 7 = **163.71428571428572**

Average height rounded to the nearest whole number = 164

**Important** You should not use the ```sum()``` or ```len()``` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

## Example Input

---

```
156 178 165 171 187
```

In this case, student_heights would be a list that looks like: [156,178,165,171,187]

## Example Output

---

```
171
```

## Hint

---

1. Remember to use the ```round()``` functions to round the average height beofre you print it.

## Test Your Code

---

Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-5-1-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

## Solution

---

https://repl.it/@appbrewery/day-5-1-solution

---

# Highest Score

---

## Instructions

---

You are going to write a program that calculates the highest score from a List of scores.

e.g. ```student_score = [78, 65, 89, 86, 55, 91, 64, 89]```

**Important** you are not allowed to use the max or min functions. The output words must match the example. i.e

```The highest score in the class is: x```

## Example Input

```
78 65 89 86 55 91 64 89
```

In this case, student_scores would be a list that looks like: ```[78, 65, 89, 86, 55, 91, 64, 89]```

## Example Output

---

```
The highest score in the class is: 91
```

## Hint

---

1. Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

## Test Your Code

---

Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-5-2-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

## Solution

---

https://repl.it/@appbrewery/day-5-2-solution

# Adding Evens

---

## Instructions

---

You are going to write a program that calculates the sum of all the even numbers from 1 to 100,
including 1 and 100.

e.g. 2 + 4 +6 + 8 + 10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

## Hint 

---

1. There are quite a few ways of solving this problem, but you will need to use the ```range()``` function in any of the solutions.


---

# FizzBuzz

---

## Instructions

---

You are going to write a program that automatically prints the solution to the FizzBuzz game.

```
Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5 then instead of printing the number it should print "Buzz".

And if the number is divisible by both 3 and 5 e.g. 15 then instead of number it should print "FizzBuzz".
```

e.g. it might start off like this:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

## Hint

---

1. Remember your answer should start from 1 and go up to and including 100.
2. Each number/text should be printed on a separate line.

---

# Password Generator

---

## Instructions

---

The program will ask:

```
How many letters would you like in your password?
```

```
How many symbols would you like?
```

```
How many numbers would you like?
```

The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

## Easy Version (Step 1)

---

Generate the password in sequence. If the user wants

<ul>
<li>4 letters</li>
<li>2 symbols and </li>
<li>3 numbers</li>
</ul>

then the password might look like this:

```
fgdx#*924
```

You can see that all the letters are together. All the symbols are together and all the numbers are together. Try to solve this problem first.

## Hard Version (Step 2)

---

When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

```
x#d24g*f9
```

And every time you generate a password, the positions of the symbols, numbers, and letters are different.

