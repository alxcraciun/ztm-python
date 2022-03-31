# Find user age based on current date 

from datetime import date

birth_year = input('What year where you born? ')
age = date.today().year - int(birth_year)

print(f'You are {age} years old')