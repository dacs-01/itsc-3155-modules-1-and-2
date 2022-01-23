# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This code will make the user enter a word 5 times to 
# make the inputs into a sentence. 

list = []
for i in range(5):
    word = input('Enter a word: ')
    list.append(word)
for i in list:
    print(i + ' ', end='')