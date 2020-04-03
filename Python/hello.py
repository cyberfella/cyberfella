from math import *

# My Python Examples - Matthew Bradley, Corona Virus Pandemic, March 2020
# variables
country_name = "England"
number_of_years = 2020
brexit = True
my_number = -98
# strings
print("hello " + country_name + " and welcome to the year " + str(number_of_years))
print(country_name.lower())
# math
print(2.5 + 3.2 * 5 / 2)
print(2 * (3 + 2))
print(10 % 3)
print(abs(my_number))
print(pow(3, 2))
print(max(4, 6))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(9))
# user input
name = input("Enter your name: ")
print("Hello " + name)
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) * float(num2)
print(result)
# lists
friends = ["Eldred", "Chris", "Julian", "Chris"]
friend = ["Eldred", 1, True]
print(friends)
print(friends[1])
print(friends[1:])
print(friends[1:3])
friends[1] = "Benny"
lucky_numbers = [23, 8, 90, 44, 42, 7, 3]
friends.extend(str(lucky_numbers))
friends.append("Helen")
friends.insert(1, "Sandeep")
friends.remove("Benny")
friends.pop()
print(friends.index("Julian"))
print(friends.count("Chris"))
friends.sort()
print(friends)
friends2 = friends.copy()
friends.clear()
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
# tuples
coordinates = (4, 5)
print(coordinates[0])


# functions
def hello_user(name):
    print("Hello " + name)


hello_user("Bob")


def hello_age(name, age):
    print("Hello " + name + ", you are " + str(age))


hello_age("Matt", 45)


def cube(num):
    return (num ^ 3)
    # no code after a return statement


print(cube(10))
result = (cube(4))

# if statements
is_male = True
is_tall = True

if is_male and is_tall:
    print("You're a tall male")  # executes if both variables are True
elif is_male and not (is_tall):
    print("You're male but not tall")  # executes if one but not the other are True
elif is_tall and not (is_male):
    print("You're tall but not male")
else:
    print("You're not tall or male")  # executes if neither are True


# Comparison Operators
# Function to return the biggest number of three numbers
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 4, 5))


# Function to compare three strings
def match(str1, str2, str3):
    if str1 == str2 and str1 == str3:
        return "All strings match"
    elif str1 == str2 and str1 != str3:
        return "Only the first two match"
    elif str1 != str2 and str2 == str3:
        return "Only the second two match"
    elif str1 == str3 and str1 != str2:
        return "Only the first and last match"
    else:
        return "None of them match"


print(match("Bob", "Alice", "Bob"))

# A Calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter first number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Bob", "Key not in dictionary"))

# WHILE LOOPS
x = 1
while x <= 10:
    print(x)
    x = (x + 1)  # or use x += 1 to increment by 1

print("Done with loop")

# GUESSING GAME
secret_word = "cyberfella"
guess = ""
tries = 0
limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:  # will loop code while conditions are True
    if tries < limit:
        guess = input("Enter guess: ")
        tries += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    # executes if condition/boolean variable is True
    print("Out of guesses, you lose!")
else:
    # executes if boolean condition is False
    print("You win")

# FOR LOOPS
for eachletter in "Cyberfella Ltd":
    print(eachletter)

friends = ["Bob", "Alice", "Matt"]
for eachfriend in friends:
    print(eachfriend)

for index in range(10):
    print(index)  # prints all numbers excluding 10

for index in range(3, 10):
    print(index)  # prints all numbers between 3 and 9 but not 10

for index in range(len(friends)):
    print(friends[index])  # prints out all friends at position 0, 1, 2 etc

for index in range(5):
    if index == 0:
        print("first iteration of loop")
    else:
        print("not first iteration")

# EXPONENT FUNCTIONS
print(2 ** 3)  # performs a calculation of 2 to the power of 3


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        # carry on multiplying the number by itself until you hit the range limit specified by pow_num
        result = result * base_num
    return result


# 2D Lists and Nested Loops

# Create a grid of numbers, that is 4 rows and 3 columns
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# return the value from first row (row 0) first column (position 0)
print(number_grid[0][0])
# returns 1

# return the value from third row (row 2) third column (position 2)
print(number_grid[0][0])
# returns 9

for eachrow in number_grid:
    print(eachrow)

for eachrow in number_grid:
    for column in eachrow:
        print(column)


# returns the value of each column in each row until it hits the end

# BUILD A TRANSLATOR
# CONVERTS ANY VOWELS TO A X
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input, that number entered is likely not an integer")
except ZeroDivisionError as err:
    print(err)

# READING FROM FILE
employee_file = open("employees.txt", "r")  # opens file read mode
print(employee_file.readable())  # checks file is readable
print(employee_file.read())  # reads entire file to screen
print(employee_file.readline())  # can be used multiple times to read next line in file
print(employee_file.readlines())  # reads each line into a list
print(employee_file.readlines()[1])  # reads into a list and displays item at position 1 in the list
employee_file.close()  # closes file

for employee in employee_file.readlines():
    print(employee)
employee_file.close()

# WRITING AND APPENDING TO FILE
employee_file = open("employees.txt", "a")  # opens file append mode
employee_file.write(
    "Toby - HR")  # in append mode will append this onto the end of the last line, not after the last line
employee_file.write(
    "\nToby - HR")  # in append mode will add a newline char to the end of the last line, then write a new line

employee_file = open("employees.txt", "w")  # opens file write mode
employee_file.write("Toby - HR")  # in write mode, this will overwrite the file entirely

employee_file.close()

# IMPORTING FUNCTIONS FROM EXTERNAL FILES

import useful_tools

print(useful_tools.rolls_dice(10))
# MORE MODULES AT docs.python.org/3/py-modindex.html

# SOME USEFUL COMMANDS
feet_in_mile = 5280
metres_in_kilometer = 1000
beatles = ["John", "Ringo", "Paul", "George"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)


# CLASSES

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


# BUILDING A MULTIPLE CHOICE QUIZ
from Question import Question

question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are Bananas\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)

#OBJECT CLASSES
from Student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)
