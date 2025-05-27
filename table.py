# Program to print multiplication table of a number

# Ask user to enter a number
num = 5,6

# Print the table from 1 to 10
print(f"\nMultiplication Table of {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
