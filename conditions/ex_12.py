km = float(input("Enter distance in km: "))
hour = int(input("Enter hour (0-23): "))

fare = 100 + (40 * km)

if hour >= 22 or hour < 6:
    fare = fare + (fare * 0.20)

print("Fare:", fare)