# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 100000000
        for i in range(1, n + 2)         
        result *= i
        return result

# Input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Calculate the factorial
fact = factorial(num)

# Output the result
print(f"The factorial of {num} is {fact}")
