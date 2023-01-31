# inp = input('Enter Fahrenheit Temperature: ')
# fahr = float(inp)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)

# inp = input('Enter Fahrenheit Temperature: ')
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Please enter a number')

# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# askhour = 'How many hours are you staying\n'
# hour = input(askhour)
# ahour = int(hour)
# askrate = 'How much are you paying\n'
# rate = input(askrate)
# hourlyrate = float(rate) * 1.5
# total = ahour * hourlyrate
# print(f'Gross pay: {total}')


# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

# askhour = 'How many hours are you staying\n'
# askrate = 'How much are you paying\n'
# try:
#     hour = input(askhour)
#     ahour = int(hour)
#     rate = input(askrate)
#     hourlyrate = float(rate) * 1.5
#     total = ahour * hourlyrate
#     print(f'Gross pay: {total}')
# except:
#     print('please enter numeric input')


# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

# Score    Grade
# >= 0.9   A
# >= 0.8   B
# >= 0.7   C
# >= 0.6   D
# < 0.6    F

prompt = 'Enter a score: '
score = input(prompt)
try:
    grade = float(score)
    A = 0.9
    if grade > 0.0 and grade < 1.0:
        if grade >= A:
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
        print('Bad score')
except:
    print('bad score')
