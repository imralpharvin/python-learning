# Name: Ralph Arvin De Castro
# Date: January 06, 2019
# Program: This program determines first digit number in the string

string = input("Please input string: ")

for charElem in string:
    if charElem.isdigit():
        print("The first number in your string is", charElem)
        break

else:
    print("Your string does not have a number")