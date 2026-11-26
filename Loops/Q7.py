products = [
    ("Laptop", 150000, 3),
    ("Mouse", 2500, 0),
    ("Keyboard", 5000, 12),
    ("Monitor", 45000, 2)
]

out_of_stock = []
low_stock = []
total_value = 0


for name, price, quantity in products:
    
    if quantity == 0:
        out_of_stock.append(name)
    elif 1 <= quantity <= 4:
        low_stock.append(name)
        
  
    total_value += price * quantity


print(f"out of stock {', '.join(out_of_stock)} · low stock {', '.join(low_stock)} · total {total_value}")
