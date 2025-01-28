cart = [] 

while True:
    print("1. Add Item")
    print("2. View Cart")
    print("3. Exit")
    choice = input("Enter your choice:\n")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.append((item, price))
        print(f"{item} added to the cart.")
        
    elif choice == "2":
        if not cart:
            print("Your cart is empty.")
        else:
            print("Items in your cart:\n")
            for item, price in cart:
                print(f"{item}: ${price:}")
            total = sum(price for _, price in cart)
            print(f"Total Price: ${total:}")

    elif choice == "3":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice")
