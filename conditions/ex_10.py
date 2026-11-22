balance = float(input("Enter balance: "))
price = float(input("Enter package price: "))

if balance >= price:
    print("Package activated")
    print("Remaining balance:", balance - price)
else:
    print("Insufficient balance, need Rs", price - balance, "more")