"""
Lesson Outline: Arguments passing in Python functions

5 types of arguments:

1. default arguments

2. fixed keyword arguments
3. fixed positional arguments

4. arbitrary keyword arguments
5. arbitrary positional arguments
"""

import random


# Parametrised function (a function that accepts input(s))
# This function has 2 parameters
def generateMathQuestion(num1, num2):
    # operatorList = ['+', '-', '*', '/']

    operator = random.randint(1, 4)

    if operator == 1:
        answer = input("What's  " + str( num1) + ' + 0' + str(num2) + '?')
        if int(answer) == num1 + num2:
            print("Good Job. Let's move on to the next question")

        else:
            print("Bad Job. Try Again!")

    elif operator == 2:
        answer = input("What's " + str(num1) + ' - ' + str(num2) + '?')
        if int(answer) == num1 - num2:
            print("Good Job. Let's move on to the next question")

        else:
            print("Bad Job. Try Again!")

    elif operator == 3:
        answer = input("What's " + str(num1) + ' * ' + str(num2) + '?')
        if int(answer) == num1 * num2:
            print("Good Job. Let's move on to the next question")

        else:
            print("Bad Job. Try Again!")

    elif operator == 4:
        print('Specify your answer in 1 decimal precision')
        answer = input("What's " + str(num1) + ' / ' + str(num2) + '?')
        if int(answer) == format(num1 / num2, '.1f'):
            print("Good Job. Let's move on to the next question")

        else:
            print("Bad Job. Try Again!")



while True:
        generateMathQuestion( random.randint(1, 1000), (random.randint(1, 1000)))

