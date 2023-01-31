# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count: ', count)

# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# print(len(fhand.read()))
# print(len(fhand.read()))

# for line in fhand:
#     if line.startswith('From'):
#         print(line)

# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)


# for line in fhand:
#     line = line.rstrip()
#     # Skip 'uninteresting lines'
#     if not line.startswith('From:'):
#         continue
#     # Process our 'interesting' line
#     print(line)

# for line in fhand:
#     line = line.rstrip()
#     if line.find('@uct.ac.za') == -1:
#         continue
#     print(line)


# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# fout = open('output.txt', 'w')
# # print(fout)
# line1 = "This here's the wattle, \n"
# line2 = 'the emblem of our land.\n'
# fout.write(line1)
# fout.write(line2)
# fout.close()

# s = '1 2\t 3\n 4'
# print(s)
# print(repr(s))


# Exercise 1:
# Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will
# look as follows:

# fname = input('Enter a file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File doesnot exist')
#     exit()
# for line in fhand:
#     print(line.upper())

# Exercise 2:
# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.
# fname = input('Enter a file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File doesnot exist')
#     exit()

# total = 0
# average = 0
# count = 0


# for line in fhand:
#     line = line.strip()
#     if line.startswith('X-DSPAM-Confidence:'):
#         colon_pos = line.find(':')
#         ext_num = float(line[colon_pos+1:])
#         total = total + ext_num
#         count = count + 1
#         average = total / count
# print('Average spam confidence:', round(average, 4))


# Exercise 3:
#  Sometimes when programmers get bored or want to have a
# bit of fun, they add a harmless Easter Egg to their program. Modify
# the program that prompts the user for the file name so that it prints a
# funny message when the user types in the exact file name “na na boo
# boo”. The program should behave normally for all other files which
# exist and don’t exist. Here is a sample execution of the program:

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    elif 'txt' in fname:
        print('File cannot be opened: ', fname)
    else:
        print('fuckoff')

    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
