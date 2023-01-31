import random
import math

# for i in range(10):
#     x = random.random()
#     print(x)


# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')


# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()


# repeat_lyrics()


def print_twice(bruce):
    print(bruce)
    print(bruce)


# michael = 'Eric, the half a bee.'
# print_twice(michael)


# Fruitful functions and void functions
# x = math.cos(radians)
# golden = (math.sqrt(5) + 1) / 2

# math.sqrt(5)

# result = print_twice('Bing')
# print(result)

# print(type(None))


# def addtwo(a, b):
#     added = a + b
#     return added


# x = addtwo(3, 5)
# print(x)

# Exercise 1:
# Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.

# for i in range(3):
#     x = random.random()
#     print(x)


# Exercise 4: What is the purpose of the “def” keyword in Python?
# answer:  It indicates the start of a function

# Exercise 5: What will the following Python program print out?
# def fred():
#     print("Zap")


# def jane():
#     print("ABC")


# jane()
# fred()
# jane()

# answer : ABC Zap ABC

# Exercise 6:
# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate)


# prompt = 'Enter Hours: '
# prompt1 = 'Enter Rate: '


# def computepay(hours, rate):
#     hour = input(prompt)
#     rate = input(prompt1)
#     hourly = int(hour)
#     rately = float(rate)
#     pay = hourly * rately
#     return pay


# x = computepay(45, 10)
# print(x)

# Exercise 7:
# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string


def computegrade(score):
    ask = input('Enter score: ')
    try:
        grade = float(ask)
        if grade > 0.0 and grade < 1.0:
            if grade >= 0.9:
                print('A')
            elif grade >= 0.8:
                print('B')
            elif grade >= 0.7:
                print('C')
            elif grade >= 0.6:
                print('D')
            elif grade < 0.6:
                print('F')
        else:
            print('Bad score 1')
    except:
        print('Bad score')

    return score


computegrade('score')
