balance = 10000
history = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount

        history.append("Deposited: Rs. " + str(amount))
        print("Deposit successful")

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))

        if amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
            history.append("Withdrawn: Rs. " + str(amount))
            print("Withdrawal successful")

    elif choice == "3":
        print("Current balance: Rs.", balance)

    elif choice == "4":
        print("Transaction History:")

        for transaction in history:
            print(transaction)

        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")