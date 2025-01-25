number = int(input("Enter the number for the multiplication table:\n"))
start = int(input("Enter the starting range:\n"))
end = int(input("Enter the ending range:\n"))

for i in range(start, end + 1):
    print(f"{number} x {i} = {number * i}")
