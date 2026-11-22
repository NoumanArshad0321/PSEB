matric = float(input("Enter Matric percentage: "))
inter = float(input("Enter Inter percentage: "))
test = float(input("Enter entry test marks: "))

if (matric >= 60 and inter >= 50) or test >= 70:
    print("Eligible")
else:
    print("Not eligible")