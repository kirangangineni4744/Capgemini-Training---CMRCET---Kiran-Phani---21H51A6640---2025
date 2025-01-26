def generate_pattern(n, reverse=False):
    if reverse:
        for i in range(n, 0, -1):
            print("*" * i)
    else:
        for i in range(1, n + 1):
            print("*" * i)

n = int(input("Enter the number of rows:\n"))
reverse = input("Do you want the pattern in reverse? (yes/no): ").lower()

if reverse == "yes":
    generate_pattern(n, reverse=True)
else:
    generate_pattern(n)
