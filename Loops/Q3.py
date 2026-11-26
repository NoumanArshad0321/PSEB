prices = [450, 1200, 980,300, 75]
hp=prices[0]
lp=prices[0]

for i in prices:
    if i > hp:
        hp = i
        
    if i < lp:
        lp=i
            
print("highest price:",hp)        
print("lowest price:",lp)