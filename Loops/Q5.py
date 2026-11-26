students = {"Ali": 85, "Sara": 92, "Ahmed": 76, "Hina": 58, "Bilal": 64}

results = []

for name, score in students.items():
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    results.append(f"{name} {grade}")

average = sum(students.values()) / len(students)

print(", ".join(results))
print(f"Average: {average}")
