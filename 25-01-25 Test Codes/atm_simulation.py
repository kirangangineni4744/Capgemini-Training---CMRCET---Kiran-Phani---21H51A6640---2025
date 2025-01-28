balance = 0

def check_balance():
    print(f"Your current balance is:{balance:.2f}/-")

def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"{amount:.2f}/- deposited successfully.")
    else:
        print("Invalid deposit")

def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance")
    elif amount <= 0:
        print("Invalid withdrawal amount")
    else:
        balance -= amount
        print(f"{amount:.2f}/- withdrawn successfully")

while True:
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
