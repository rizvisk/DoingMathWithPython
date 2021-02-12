'''
Unit Converter (Extended)
'''


def menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celcius to Fahrenheit')
    print('6. Fahrenheit to Celcius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = (km / 1.609)
    miles = '{0:.2f}'.format(miles)

    print('Distamce in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    km = '{0:.2f}'.format(km)

    print('Distance in kilometers: {0}'.format(km))

def kg_pounds():
    kg = float(input('Enter weight in kilograms: '))
    pounds = kg * 2.205
    pounds = '{0:.2f}'.format(pounds)

    print('Weight in pounds: {0}'.format(pounds))

def pounds_kg():
    pounds = float(input('Enter weight in pounds: '))
    kg = pounds / 2.205
    kg = '{0:.2f}'.format(kg)

    print('Weight in kg: {0}'.format(kg))

def C2F():
    C = float(input('Enter temp in Celcius: '))
    F = (C * 9/5) + 32
    F = '{0:.2f}'.format(F)

    print('Temp in Fahrenheit: {0}'.format(F))

def F2C():
    F = float(input('Enter temp in Fahrenheit: '))
    C = (F - 32) * 5/9
    C = '{0:.2f}'.format(C)

    print('Temp in Celcius: {0}'.format(C))

menu()
choice = input('Whice conversion would you like to do? ')
if choice == '1':
    km_miles()

if choice == '2':
    miles_km()

if choice == '3':
    kg_pounds()

if choice == '4':
    pounds_kg()

if choice == '5':
    C2F()

if choice == '6':
    F2C()
