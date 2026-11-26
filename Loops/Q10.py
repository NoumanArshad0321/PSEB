cart = {}

while True:
    print("\n1. Add item")
    print("2. View cart")
    print("3. Checkout")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        price = int(input("Enter item price: "))

        cart[name] = price
        print("Item added!")

    elif choice == "2":
        total = 0

        for name, price in cart.items():
            print(name, "Rs.", price)
            total = total + price

        print("Total: Rs.", total)

    elif choice == "3":
        total = 0

        for price in cart.values():
            total = total + price

        print("Total: Rs.", total)

        if total > 5000:
            discount = total * 0.10
            total = total - discount
            print("Discount: Rs.", discount)

        print("Final bill: Rs.", total)
        break

    else:
        print("Invalid choice")