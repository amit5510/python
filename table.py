# Program to print multiplication table of a number

# Ask user to enter a number
num = int(input("Enter a number to print its multiplication table: "))

# Print the table from 1 to 10
print(f"\nMultiplication Table of {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
