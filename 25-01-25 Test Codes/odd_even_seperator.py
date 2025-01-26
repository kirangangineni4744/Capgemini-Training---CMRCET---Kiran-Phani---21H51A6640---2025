def separate_odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return odd_numbers, even_numbers

numbers = list(map(int, input("Enter numbers separated by spaces:\n").split()))

odd_numbers, even_numbers = separate_odd_even(numbers)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
