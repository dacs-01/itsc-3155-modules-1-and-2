# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This code contains a loop of a list that only ends when the user tells it to quit.
# The user can type any integer, but only even integers will be added to a list.
# Once the user ends the code, the list will be printed with all even integers.

list = []
boo = True
while (boo):
    val = input('Enter a value or QUIT: ')
    if (val == 'QUIT' or val == 'quit'):
        boo = False
        print(list)
    else:
        val = int(val)
        if (val % 2 == 0):
            list.append(val)

