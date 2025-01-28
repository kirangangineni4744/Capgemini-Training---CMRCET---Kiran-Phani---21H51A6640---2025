password = input("Enter a password:\n")

if len(password)<8:
    print("Weak Password")
elif password.lower()==password:
    print("Weak Password")
elif password.upper()==password:
    print("Weak Password")
elif not any(char.isdigit() for char in password):
    print("Weak Password")
elif not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
    print("Weak Password")
else:
    print("Strong Password")
