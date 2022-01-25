# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This program gets all of the upper case letters of an inputted string
# and moves them all to the end of a new string. 
# (This code was inpsired from GeeksForGeeks https://www.geeksforgeeks.org/move-all-uppercase-char-to-the-end-of-string/)

given_input = input('Enter a string or strings to move capitalization: ')
lc = '' # variable that holds lowercase letters
uc = '' # variable that holds uppercase letters
for i in range(0, len(given_input), 1): # loop that iterates thru inputted string
    if given_input[i] >= 'A' and given_input[i] <= 'Z':
        uc += given_input[i] # add all uppercase letters to upper case variable
    elif given_input[i] != ' ':
        lc += given_input[i] # add all lowercase letters to lower case variable and remove spaces
print(lc + uc)