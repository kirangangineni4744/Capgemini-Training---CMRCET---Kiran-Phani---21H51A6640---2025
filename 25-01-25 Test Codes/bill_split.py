total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
tip_percent = float(input("Enter the tip percentage: "))

if num_people > 0:
    total_with_tip = total_bill + (total_bill * tip_percent / 100)
    amount_per_person = total_with_tip / num_people
    print(f"Each person should pay: ₹{amount_per_person:.2f}")
else:
    print("Number of people must be greater than 0.")
