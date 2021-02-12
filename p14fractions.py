'''
Fraction Operations
'''

from fractions import Fraction


def add(a, b):
    print('Result of Addition: {0}'.format(a+b))


def subtraction(a, b):
    print('Result of Subtraction: {0}'.format(a-b))


def multiply(a, b):
    print('Result of Multiplication: {0}'.format(a*b))


def divide(a, b):
    print('Dividing first number by second')
    print('Result of Division: {0}'.format(a/b))


while True:
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter second fraction: '))
    op = input('Operation to perform - +, -, *, /: ')

    if op == '+':
        add(a, b)

    if op == '-':
        subtraction(a, b)

    if op == '*':
        multiply(a, b)

    if op == '/':
        divide(a, b)

    answer = input('Do you want to exit? (y) for yes ')
    if answer == 'y':
        break
