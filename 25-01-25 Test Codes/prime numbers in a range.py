def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

start = int(input("Enter the start number:\n"))
end = int(input("Enter the end number:\n"))

print(f"Prime numbers between {start} and {end}:")
prime_numbers_in_range(start, end)
