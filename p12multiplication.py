'''
Multiplication table printer
'''


def multi_table(a, b):

    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))


try:

    while True:
        a = int(input('Enter a number: '))
        b = int(input('How many multiples? '))
        multi_table(a, b)

        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break


except ValueError:
    print('Please enter a number')
