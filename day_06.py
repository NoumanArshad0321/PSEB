fruits=["apple", "banana", "cherry"]
for i in range(3):
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


student_name = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis"]
# print(type(student_name))  # Output: <class 'list'>
print(student_name)  # Output: ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis']
print(f"First three students in {student_name} are follows:", student_name[0:3])
  # Output: ['John Doe', 'Jane Smith', 'Alice Johnson'] (accessing the first three elements of the list)

# negative indexing
print(f"Last student in {student_name} is:", student_name[-1])

# slicing with step
print(f"Every second student in {student_name} is:", student_name[::2])  # Output: ['John Doe', 'Alice Johnson', 'Charlie Davis'] (accessing every second element of the list)


# Assigning a new value to an existing index
student_name[1] = "Samiullah"
print(f"After changing the second student name in {student_name} is:", student_name)  # Output: ['John Doe', 'Samiullah', 'Alice Johnson', 'Bob Brown', 'Charlie Davis'] (changing the second element of the list)

# appending a new value to the list
student_name.append("David Wilson")
print(f"After appending a new student in {student_name} is:", student_name)  # Output: ['John Doe', 'Samiullah', 'Alice Johnson', 'Bob Brown', 'Charlie Davis', 'David Wilson'] (appending a new element to the list)

# popping the last value from the list
student_name.pop()
print(f"After popping the last student in {student_name} is:", student_name)


# removing a specific value from the list
student_name.remove("Samiullah")
print(f"After removing the second student name in {student_name} is:", student_name)  # Output: ['John Doe', 'Alice Johnson', 'Bob Brown', 'Charlie Davis'] (removing a specific element from the list)


# for clearing the list
student_name.clear()
print("After clearing the list  is:", student_name)  # Output: [] (clearing all elements from the list)


names = ["Ali", "Ahmed", "Ayesha", "Fatima", "Hassan", "Hussain"]
print(names)  # Output: ['Ali', 'Ahmed', 'Ayesha', 'Fatima', 'Hassan', 'Hussain']
list_length = len(names)  # Getting the length of the list
print(f"Length of the list {names} is:", list_length)  # Output: 6 (getting the length of the list)
names.sort()  # Sorting the list in ascending order
print(f"After sorting the list {names} is:", names)  # Output: ['Ahmed', 'Ali', 'Ayesha', 'Fatima', 'Hassan', 'Hussain'] (sorting the list in ascending order)
names.reverse()  # Reversing the list
print(f"After reversing the list {names} is:", names)  # Output: ['Hussain', 'Hassan', 'Fatima', 'Ayesha', 'Ali', 'Ahmed'] (reversing the list)
del names[0]  # Deleting the first element of the list
print(f"After deleting the first element of the list {names} is:", names)  # Output: ['Hassan', 'Fatima', 'Ayesha', 'Ali', 'Ahmed'] (deleting the first element of the list)




# tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed. This makes tuples useful for representing fixed collections of items.
student_info = ("John Doe", 20, "Computer Science")  # Creating a tuple
print(f"Student info: {student_info}")  # Output: Student info: ('John Doe', 20, 'Computer Science')

print(f"First element of the tuple {student_info} is:", student_info[0])  # Output: John Doe (accessing the first element of the tuple)
print(f"Last element of the tuple {student_info} is:", student_info[-1])  # Output: Computer Science (accessing the last element of the tuple)
print(f"Length of the tuple {student_info} is:", len(student_info))  # Output: 3 (getting the length of the tuple)
print(f"Count of 'John Doe' in the tuple {student_info} is:", student_info.count("John Doe"))  # Output: 1 (counting occurrences of an element in the tuple)
print(f"Index of 'Computer Science' in the tuple {student_info} is:", student_info.index("Computer Science"))  # Output: 2 (getting the index of an element in the tuple)
print(f"Every second element in the tuple {student_info} is:", student_info[::2])  # Output: ('John Doe', 'Computer Science') (accessing every second element of the tuple)
print(f"Every element in the tuple {student_info} is:", student_info[:])  # Output: ('John Doe', 20, 'Computer Science') (accessing all elements of the tuple)


# converting a list to a tuple
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)  # Converting the list to a tuple
print(f"List {fruits_list} converted to tuple is:", fruits_tuple)  # Output: ('apple', 'banana', 'cherry')
print(f"Type of {fruits_list} is:", type(fruits_list))  # Output: <class 'list'> (checking the type of the list)
print(f"Type of {fruits_tuple} is:", type(fruits_tuple))  #Output: <class 'tuple'> (checking the type of the tuple)
print(f"Length of the tuple {fruits_tuple} is:", len(fruits_tuple))  # Output: 3 (getting the length of the tuple)