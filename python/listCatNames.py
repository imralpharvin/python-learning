# Name: Ralph Arvin De Castro
# Date: January 09, 2019
# Program: This program manages a list of cat names


def addCat(list, name):
    """
    This function adds a cat in the list.
    """
    list.append(name)

def removeCat(list, name):
    """
    This function removes a cat from the list.
    """
    list.remove(name)

def printCatNames(list):
    """
    This function prints the list of cat names
    """
    print("The name of the " + str(len(list)) + " cats are " + ', '.join(list) + ".")


catNames = []

selected = 'O'

while selected != 'q':

    selected = input("What would you like to do?\n1: Add a cat\n2: Print list of cats\n3: Remove a cat\n\nq: Quit\n")

    if(selected == '1'):
        cat = input("Please enter the name of the cat: ")
        addCat(catNames, cat)

    elif(selected == '2'):
        printCatNames(catNames)

    elif(selected == '3'):
        cat = input("Please enter the name of the cat: ")
        removeCat(catNames, cat)

    elif(selected == 'q'):
        print("Thank you and have nice day!")
        break