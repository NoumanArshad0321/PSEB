print("*********************Voting Eligibility************************************")


age = int(input("Enter your age in numbers:"))


if age >= 18:
    print(f"You are eligible to vote as you are {age} years old.")
else:
    left_years=18-age
    print(f"Not eligible wait {left_years} years  to vote.")

