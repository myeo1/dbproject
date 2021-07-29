# Basic addition calculator
try:
    # Get the first number
    number_input = input('Enter the first number: ')
    # Parse the string input as an integer
    number_one = int(number_input)

# In case the user doesn't give an integer

except:
    number_one = int(input('Please enter a whole number: '))

# Repeat the process for the second number
try:
    number_input = input('Enter the second number: ')
    number_two = int(number_input)
except:
    number_two = int(input('Please enter a whole number: '))


# Add the numbers together as part of the output
print('The answer is', number_one + number_two)