# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This code asks the user to input any integer greater than 0
# and returns every number from 0 to that inputted number,
# as well as each of those numbers squared.

num = int(input('Enter an integer greater than 0: '))
if num >= 1:
    for i in range(num + 1):
        print('The square of ' + str(i) + ' is ' + str(i*i))
else:
        print("Follow directions this time; enter an integer greater than 0. Hit play again.")

