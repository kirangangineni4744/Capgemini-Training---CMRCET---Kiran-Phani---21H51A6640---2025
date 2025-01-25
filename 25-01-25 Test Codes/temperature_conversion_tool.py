def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_conversion():
    choice = input("Choose the option (1-6):\n")
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius:\n"))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius:\n"))
        print(f"{celsius}°C = {celsius_to_kelvin(celsius)}K")
    elif choice == "3":
        fahrenheit = float(input("Enter temperature in Fahrenheit:\n"))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")
    elif choice == "4":
        fahrenheit = float(input("Enter temperature in Fahrenheit:\n"))
        print(f"{fahrenheit}°F = {fahrenheit_to_kelvin(fahrenheit)}K")
    elif choice == "5":
        kelvin = float(input("Enter temperature in Kelvin:\n"))
        print(f"{kelvin}K = {kelvin_to_celsius(kelvin)}°C")
    elif choice == "6":
        kelvin = float(input("Enter temperature in Kelvin:\n"))
        print(f"{kelvin}K = {kelvin_to_fahrenheit(kelvin)}°F")
    else:
        print("Invalid choice")

temperature_conversion()
