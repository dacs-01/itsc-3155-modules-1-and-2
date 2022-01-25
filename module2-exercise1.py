# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This program prints out a given string in reverse by using 
# a slice that goes backwards, starting at end of string all the way to position 0.
# (This code was inspired from W3schools https://www.w3schools.com/python/python_howto_reverse_string.asp)

word = input('Enter a string to reverse: ')[::-1]
print(word)