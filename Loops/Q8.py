nums = [3, 5, 3, 8, 5, 3, 9]

count = {}

for n in nums:
    count[n] = count.get(n, 0) + 1

print("Unique numbers:", list(count.keys()))

most = max(count, key=count.get)

print("Most frequent:", most, "(", count[most], "times )")