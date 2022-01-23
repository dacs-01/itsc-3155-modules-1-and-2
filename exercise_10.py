# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This code makes the user input a word or sentence that gets
# split into blocks of 3 letters. Each character is added into 
# the list and a loop will split up those characters into chunks of 3.

list = []
word = input('Enter a word or sentence to split: ')
for i in word:
    list.append(i)
result = [list[i:i + 3] for i in range(0, len(list), 3)]
print (result)