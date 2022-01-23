# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# There is a 5x5 matrix of 0s created and the user will input
# a specified coordinate which will turn that 0 into a 1.

row = int(input('Enter a row num from 1 to 5: '))
col = int(input('Enter a col num from 1 to 5: '))
mat = [([0]*5) for i in range (5)]
mat[row-1][col-1]=1
for i in mat:
    print(*i, sep=' ')

