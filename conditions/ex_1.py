number = int(input("Enter a number: "))


if number == 0:
    group="zero"
elif number > 0:
    group="positive"
else:
    group ="negative"    
print(f"The number {number} is {group}.")


