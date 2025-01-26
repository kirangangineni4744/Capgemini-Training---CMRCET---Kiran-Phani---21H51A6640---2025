def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    number = int(input("Enter a number:\n"))
    if number == -1:
        break
    elif number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {number} is {factorial(number)}")
