print("My age: " + str(23))
print(12 + 11) # addition
print(30 - 7) # subtraction
print(11 * 2) # multiplication
print(44 / 2) # division - forward slash not backslash, always return float, even if the number is a whole number
print(44 // 2) # division v2 - performs division but then removes all of the decimal places. DANGEROUS if the division isn't clean
print(4 ** 2) # exponential - raises the first number to the power of the second number

# Python follows the PEMDAS order from early school years. LEFT -> RIGHT
print(3 * 3 + 3 / 3 - 3) # answer should be 7.0 due to the type being converted to float because of the division operand

# Change the ^above code^ so that it outputs 3.0
print(3 * (3 + 3) / 3 - 3)