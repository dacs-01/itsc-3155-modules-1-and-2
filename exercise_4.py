# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This code asks the user to enter an integer of how many floats
# they want to input. After that, the user will enter each float
# into a list and the code will print the list and calculate the 
# average from the list.

amount = int(input('Enter a number: '))
lst = []
for i in range(1,amount+1):
    element = float(input('Enter float element number ' + str(i) + ': '))
    lst.append(element)
print('List: ' + str(lst))
average = sum(lst)/len(lst)
print('Average of list: ' + str(average))
