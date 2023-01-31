# print('Hello, World!')
# Python 35 keywords:
# and, del, from, None, True, as , elif, global, nonlocal, try, assert, else, if , not, while, break, except, import, or , with,
# class, False, in, pass, yield, continue , finally, is, raise, async, def, for, lambda, return, await

# print(1)
# x = 2
# print(x)

# python operators +, -, *, /, and ** perform addition, subtraction, multiplication,
# division, and exponentiation

# The word
# mnemonic 2 means “memory aid”.
# for word in words:
#     print(word)

# for slice in pizza:
#     print(slice)


# Exercise 2:
# Write a program that uses input to prompt a user for their name and then welcomes them.

# # name = input('what is your name\n')
# # print('Hello ' + name)


# Exercise 3:
# Write a program to prompt the user for hours and rate per hour to compute gross pay.

# askhour = 'How many hours are you staying\n'
# hour = input(askhour)
# int(hour)
# askrate = 'How much are you paying\n'
# rate = input(askrate)
# float(rate)
# total = int(hour) * float(rate)
# print(f'Gross pay: {total}')


# # Exercise 4:

# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# # For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# red = width//2
# print(red, type(red))
# number = width/2.0
# print(number, type(number))
# tall = height/3
# print(tall, type(tall))
# addnum = 1 + 2 * 5
# print(addnum, type(addnum))


# Exercise 5:
# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
