fruit = 'banana'
length = len(fruit)
last = fruit[length - 1]
# # print(last)

# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     index = index + 1
#     print(letter)


# Exercise 1:
# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
# index = len(fruit) - 1
# while index >= 0:
#     letter = fruit[index]
#     index = index - 1
#     print(letter)

# for char in fruit:
#     print(char)

# Exercise 2:
# Given that fruit is a string, what does fruit[:] mean?]


# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

# def countLetters(string, letter):
#     count = 0
#     for str in string:
#         if str == letter:
#             count = count + 1
#     return count


# word = input('Enter a String: ')
# alphabet = input('Enter letter: ')
# print('Count: ', countLetters(word, alphabet))


# Exercise 4:
# There is a string method called count that is similar tothe function in the previous exercise. Read the documentation of this method at:
# https://docs.python.org/library/stdtypes.html#string-methods
# Write an invocation that counts the number of times the letter a occurs in “banana”.

# line = 'banana'
# newLine = line.count('a')
# print(newLine)


# Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
newstr = str.find(':')
print(newstr)
nestr = float(str[newstr+1:])
print(nestr)
print(type(nestr))
