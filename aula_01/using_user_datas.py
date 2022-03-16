"""
How to receiving user datas from terminal
"""

# Data Input

"""
print("What is your name? ")
name = input()

print("What is your age?")
age = input()
"""

name = input('What is your name? ')
age = int(input('Whats is your age? '))

# Data Processing

# Data Output
# Old Print Exemple Version 2.x
print('%s has %s years' % (name, age))

# New Print Version 3.x
print('{0} has {1} years'.format(name, age))

# New Print Version 3.7.x I guess
print(f'{name} has {age} years')
print(f'{name} was born in {2022 - age}')
