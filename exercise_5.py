# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# Two lists are created to see which numbers are the same in both.
# This is done by getting the user to input 5 integers for each list,
# then by getting the intersection of each list.

list_1 = []
list_2 = []
for i in range(5):
    num = int(input('Enter a number for the first list: '))
    list_1.append(num)
for i in range(5):
    num_2 = int(input('Enter a number for the second list: '))
    list_2.append(num_2)
l1_as_set = set(list_1)
intersect = l1_as_set.intersection(list_2)
intersect_as_list = list(intersect)
print(intersect_as_list)