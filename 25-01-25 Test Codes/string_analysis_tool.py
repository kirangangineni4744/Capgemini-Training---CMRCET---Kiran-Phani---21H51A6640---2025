string = input("Enter a string:")

vowels = consonants = digits = special_chars = 0

for char in string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    else:
        special_chars += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Special Characters: {special_chars}")
print(f"Reversed String: {string[::-1]}")
