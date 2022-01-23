# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This code returns a letter grade for an inputted float between 0 and 100.

grade = float(input('Enter a grade between 0 and 100: '))

if grade >= 90:
    print('You have an A')
elif grade >= 80:
    print('You have a B')
elif grade >= 70:
    print('You have a C')
elif grade >= 60:
    print('You have a D')
else:
    print('You have a F')