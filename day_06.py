fruits=["apple", "banana", "cherry"]
for i in range(2):
    print(fruits[i])




subjects = ["Math", "Science", "History", "English"]
append_result = subjects.append("Art")  # Appends "Art" to the list
print(subjects)  # Output: ['Math', 'Science', 'History', 'English', 'Art']




numbers = [1, 2, 3, 4, 5]

print(numbers)  # Output: [1, 2, 3, 4, 5]

numbers.pop()  # Removes and returns the last item (5)
print("By use of pop() method it removes the last value:", numbers)  # Output: [1, 2, 3, 4]


numbers.remove(2)  # Removes the first occurrence of 2
print("By use of remove() method it removes the value 2:", numbers)  # Output: [1, 3, 4]

numbers.clear()  # Removes all items from the list
print("By use of clear() method it removes all the values in the list:", numbers)


numbers.extend([6, 7, 8])  # Extends the list by appending elements from the iterable
print("By use of extend() method it adds the values 6,7,8 in    the list:", numbers)  # Output: [6, 7, 8]


