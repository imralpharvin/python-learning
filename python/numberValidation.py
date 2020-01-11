# Name: Ralph Arvin De Castro
# Date:January 5, 2019
# Program: This program asks for number input and tells if it is between 0 to 100

numValue = int(input("Please enter a number: "))

if numValue < 0:
    print('Your number ' + str(numValue) + ' is below 0')

elif numValue > 100:
    print('Your number ' + str(numValue) + ' is greater than 100')

else:
    print('Your number ' + str(numValue) + ' is between 0 and 100')