def min_max(numbers):
    low = numbers[0]
    high = numbers[0]

    for num in numbers:
        if num < low:
            low = num

        if num > high:
            high = num

    return low, high


low, high = min_max([45, 12, 89, 33])

print("Smallest:", low)
print("Largest:", high)
