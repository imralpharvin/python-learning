# Name: Ralph Arvin De Castro
# Date: January 05, 2019
# Program: This prints cat names

catList = []

numberOfCats = int(input("Please enter number of cat names:" ))
print("Please input cat names:")


for i in range(numberOfCats):
    cat = input()
    catList.append(cat)

print("The name of the " + str(numberOfCats) + " cats are " + ', '.join(catList) + ".")

