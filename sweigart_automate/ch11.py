# raise Exception('This is the error message.')


# Raising Exceptions
# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')

#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)


# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))

# Getting the Traceback as a String

# def spam():
#     bacon()
# def bacon():
#     raise Exception('This is the error message.')
# spam()

# import traceback
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt.')

# Assertions

# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.sort()
# ages
# [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
# assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.

# Using an Assertion in a Traffic Light Simulation

# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_16th = {'ns': 'red', 'ew': 'green'}

# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] = 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'

#     assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

# switchLights(market_2nd)

# Logging

# import logging

# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')


# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s -  %(levelname)s-  %(message)s')

# logger = logging.getLogger()

# logger.setLevel(logging.WARNING)

# # logging.disable(logging.WARNING)

# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")


# def factorial(n):
#     logging.debug('Start of factorial(%s%%)' % (n))
#     total = 1
#     # for i in range(n + 1):
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug(f'i is {i}, total is {total}')
#         # logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(%s%%)' % (n))
#     return total


# print(factorial(5))
# logging.debug('End of program')

# Logging Levels

# logging.disable(logging.CRITICAL) # disable level

# Logging to a File

# import logging
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

# Mu’s Debugger

# print('Enter the first number to add:')
# first = input()
# print('Enter the second number to add:')
# second = input()
# print('Enter the third number to add:')
# third = input()
# print('The sum is ' + first + second + third)

# import random
# heads = 0
# for i in range(1, 1001):
#     if random.randint(0, 1) == 1:
#         heads = heads + 1
#     if i == 500:
#         print('Halfway done!')
# print('Heads came up ' + str(heads) + ' times.')

# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
# toss = random.choice(('heads', 'tails'))  # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     toss = random.choice(('heads', 'tails'))
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')
