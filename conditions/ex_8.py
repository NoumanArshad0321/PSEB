char= input("Enter your charcter:")
# digi = int(char)

char=char.lower()
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
    print("Wovel")
elif char.isdigit()==True:
    print("digit")
elif not char.isalnum() and not char.isspace():
    print("Special character")


else:
    print("Invalid ")


