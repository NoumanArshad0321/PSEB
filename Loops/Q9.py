students = [
    {"name": "Ali", "marks": [80, 75, 90]},
    {"name": "Sara", "marks": [95, 88, 92]},
    {"name": "Ahmed", "marks": [55, 62, 48]}
]

topper_average = 0
topper_name = ""

for student in students:
    name = student["name"]
    marks = student["marks"]

    total = sum(marks)
    average = total / len(marks)

    if average >= 60:
        result = "Pass"
    else:
        result = "Fail"

    print(name, round(average, 2), result)

    if average > topper_average:
        topper_average = average
        topper_name = name

print("Topper:", topper_name)