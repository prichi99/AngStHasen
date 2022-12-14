# Task 6
# Write a program that reads a non-negative integer number in the decimal representation provided by the user and prints
# the octal representation of the number. For example, if the user enters 167, the output should be 247.

num_dec = int(input('Please enter a non-negative number (integer) that should be converted into the octal system.\n'))

while num_dec < 0:
    num_dec = int(input('You have to enter a non-negative number! Please enter a new value.\n'))

# convert integer to octal
num_oct = ''
div = 2     # 2 resembles arbitrary value >= 1 to start loop
while div >= 1:
    i = int(num_dec % 8)
    div = num_dec / 8
    num_dec = div
    num_oct = str(i) + num_oct

num_oct = int(num_oct)
print(f'The converted integer is: {num_oct}')

# Write a more general program that reads in a non-negative number (potentially including decimal places) in the decimal
# representation provided by the user and prints the octal representation of the number. For example, if the user enters
# 25.11, the output should be 31.0702436560507534.

float_dec = float(input('Please enter a non-negative number (float) that should be converted into the octal system.\n'))

while float_dec < 0:
    float_dec = float(input('You have to enter a non-negative number! Please enter a new value.\n'))

integer = int(float_dec)
frac = float(float_dec % 1)

# convert integer part to octal
int_oct = ''
div = 2     # 2 resembles arbitrary value >= 1 to start loop
while div >= 1:
    i = int(integer % 8)
    div = integer / 8
    integer = div
    int_oct = str(i) + int_oct

# Convert float part to octal
float_oct = ''
while float(frac % 1) != 0:
    frac = frac * 8
    float_oct = float_oct + str(int(frac))
    frac = float(frac % 1)

# Set value for decimals to avoid empty string
if int(float_dec) == float_dec:
    float_oct = '0'

# Concatenate string to resemble the float
print(f'The converted float is: {int_oct}.{float_oct}')

# We could also concatenate the string for integers and the convert it to a float. The output type would then be a float
# and not a string!
# print(float(int_oct + '.' + float_oct))
# Unfortunately, floats are limited to 16 digits, which is why the output for 25.11 would be 31.070243656050753 instead
# of 31.0702436560507534. This is why I decided to use an if statement and to return a string.
