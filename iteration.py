# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Blastoff!')

# dysfunctional infinite loop
# n = 10
# while True:
#     print(n, end=' ')
#     n = n - 1
# print('Done!')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')


# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New Year:', friend)
# print('Done!')

# count = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     count = count + 1
# print('Count: ', count)

# total = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     total = total + itervar
# print('Total: ', total)

# To find the largest value in a list or sequence, we construct the following loop:
# largest = None
# print('Before:', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest:
#         largest = itervar
#     print('Loop:', itervar, largest)
# print('Largest:', largest)

# To compute the smallest number, the code is very similar with one small change:
# smallest = None
# print('Before:', smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#     print('Loop:', itervar, smallest)
# print('Smallest:', smallest)

# def min(values):
#     smallest = None
#     for value in values:
#         if smallest is None or value < smallest:
#             smallest = value
#     return smallest

# total = 0
# count = 0
# average = 0
# while True:
#     prompt = input('Enter a number: ')
#     try:
#         if prompt == 'done':
#             print('Total: ' + str(total))
#             print('count: ' + str(count))
#             print('average: ' + str(average))

#         else:
#             count = count + 1
#             total = total + float(prompt)
#             average = total / count

#     except:
#         print('Invalid input')


largest = None
smallest = None
while True:
    prompt = input('Enter a number: ')
    try:
        if prompt == 'done':
            print('largest: ' + str(largest))
            print('smallest: ' + str(smallest))
            break

        else:
            for numbers in prompt:
                if largest is None or numbers > largest:
                    largest = numbers
            for numbers in prompt:
                if smallest is None or numbers < smallest:
                    smallest = numbers

    except:
        print('Invalid input')
