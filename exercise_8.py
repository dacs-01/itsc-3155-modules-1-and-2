# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# The code will prompt the user to enter a number 10 times.
# Each number is added to a list and if there is a number that
# is only enterred once, it is unique. A loop will iterate
# thru the list to see if those unique numbers exist and 
# input it into another list. If so, list is printed.

list = []
for i in range(10):
    num = int(input('Enter a number: '))
    list.append(num)
once = [i for i in list if list.count(i) == 1]
print(once)