'''
Even-Odd Vending Machine
Print whether the number is even or odd
Display the number followed by the next 9 even or odd numbers
'''


def EvenOdd(num):

    if num % 2 == 0:
        print('Number is Even')
        print(num)
    else:
        print('Number is Odd')
        print(num)

    count = 1
    while count <= 9:
        num = num + 2
        print(num)
        count += 1


try:
    b = float(input('Enter an Integer: '))
    if b > 0 and b.is_integer():
        EvenOdd(int(b))

    else:
        print('Please enter an integer')

except ValueError:
    print('Please enter a number')
