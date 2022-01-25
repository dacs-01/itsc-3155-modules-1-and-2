# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This code takes in 2 inputted strings and determines whether
# or not the second string is a part of the first string.

word = input('Enter a string: ')
word_2 = input('Enter another string: ')
print('First string inside of second string: ' + str(word_2.startswith(word)))
print('Second string inside of first string: ' + str(word.startswith(word_2)))