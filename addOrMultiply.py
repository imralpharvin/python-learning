# Name: Ralph Arvin De Castro
# Date: January 07, 2019
# Program: This program asks for two integer input and whether to add or multiply them

def add(n, m):
    sum = n + m

    return sum

def multiply(n,m):
    product = n*m 

    return product

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

addOrMultiply = int(input("What do you want to do?\n1: Add\n2: Multiply\n"))

if addOrMultiply == 1:
    print("The sum of", str(input1), "and", str(input2), "is", str(add(input1, input2)) )

elif addOrMultiply == 2:
    print("The product of", str(input1), "and", str(input2), "is", str(multiply(input1, input2)) )

else:
    print("Please enter 1 or 2. Please restart the program.")