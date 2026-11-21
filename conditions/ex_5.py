temp = int(input("Enter the tempreture in celsius:"))


if temp<10:
    print("Cold,wear jackect.")
elif temp == 10 and temp <=25:
    print("Pleasent.")    
elif temp == 26 and temp <=35:
    print("Warm")
else:
    print("Very hot, stay hydrated.")    