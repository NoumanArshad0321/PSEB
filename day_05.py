# In the day 5 we learned the concept of python strings and there are many methods to manipulate strings. In this file we will explore some of the string methods and how to use them effectively.


# String Methods in Python
student_name = "John Doe"
print("Student Name: " + student_name)  # Output: Student Name: John Doe
print("**********************************  for Uppercase   **********************************")
print("Student Name in Uppercase: " + student_name.upper())  # Output: Student Name: JOHN DOE
print("**********************************  for Lowercase   **********************************")
print("Student Name in Lowercase: " + student_name.lower())  # Output: john doe
print("**********************************  for Capitalization   **********************************")
print("Student Name with Capitalized First Letter: " + student_name.capitalize())  # Output: John doe
print("**********************************  for Title Case   **********************************")
print("Student Name in Title Case: " + student_name.title())  # Output: John Doe

print("**********************************  for Strip   **********************************")
print("Student Name with Leading and Trailing Whitespace Removed: " + student_name.strip())  # Output: John Doe (removes leading and trailing whitespace)

print("**********************************  for Replace   **********************************")
print("Student Name with Substring Replaced: " + student_name.replace("John", "Jane"))  # Output: Jane Doe (replaces substring)

print("**********************************  for Split   **********************************")
print("Student Name Split into a List: " + str(student_name.split(" ")))  # Output: ['John', 'Doe'] (splits the string into a list)

print("**********************************  for Find   **********************************")
print("Index of Substring 'Doe': " + str(student_name.find("Doe")))  # Output: 5 (returns the index of the substring)

print("**********************************  for Startswith   **********************************")
print("Does Student Name start with 'John'? " + str(student_name.startswith("John")))  # Output: True (checks if the string starts with the substring)

print("**********************************  for Endswith   **********************************")
print("Does Student Name end with 'Doe'? " + str(student_name.endswith("Doe")))  # Output: True (checks if the string ends with the substring)

print("**********************************  for Isalpha   **********************************")
print("Are all characters in Student Name alphabetic? " + str(student_name.isalpha()))  # Output: False (checks if all characters are alphabetic)
print("**********************************  for Isdigit   **********************************")
print("Are all characters in Student Name digits? " + str(student_name.isdigit()))  # Output: False (checks if all characters are digits)
print("**********************************  for Uppercase   **********************************")
print("Student Name in Uppercase: " + student_name.upper())  # Output: JOHN DOE
print("**********************************  for Lowercase   **********************************")
print("Student Name in Lowercase: " + student_name.lower())  # Output: john doe
print("**********************************  for Capitalization   **********************************")
print("Student Name with Capitalized First Letter: " + student_name.capitalize())  # Output: John doe
print("**********************************  for Title Case   **********************************")
print("Student Name in Title Case: " + student_name.title())  # Output: John Doe
print("**********************************  for Strip   **********************************")
print("Student Name with Leading and Trailing Spaces Removed: " + student_name.strip())  # Output: John Doe
print("**********************************  for Replace   **********************************")
print("Student Name with 'John' Replaced by 'Jane': " + student_name.replace("John", "Jane"))  # Output: Jane Doe
print("**********************************  for Count   **********************************")
print("Number of occurrences of 'o' in Student Name: " + str(student_name.count("o")))  # Output: 2 (counts occurrences of a substring)
print("**********************************  for Index   **********************************")
print("Index of Substring 'Doe': " + str(student_name.index("Doe")))
print("**********************************  for Join   **********************************")
fruits = ["apple", "banana", "cherry"]  
print(" ".join(fruits)) 

# find and index methods are similar, but find returns -1 if the substring is not found, while index raises a ValueError.



#  string slicing
print("**********************************  for Slicing at :4 **********************************")
print("First 4 characters of Student Name: " + student_name[:4])  # Output: John (slices the string to get the first 4 characters)
print("**********************************  for Slicing from 5 to 9   **********************************")
print("Characters from index 5 to 8: " + student_name[5:9])  # Output: Doe (slices the string to get characters from index 5 to 8)
print("**********************************  for negative indexing   **********************************")
print("Last 3 characters of Student Name: " + student_name[-3:])  # Output: Doe (slices the string to get the last 3 characters)
print("**********************************  for accessing last character   **********************************")
print("Last character of Student Name: " + student_name[-1])  # Output: e (accesses the last character of the string)
print("**********************************  for accessing last without -1 or not specifing end   **********************************")
print("Last character of Student Name: " + student_name[len(student_name)-1])  # Output: e (accesses the last character of the string)






# for fromatting strings we can use f-strings which is available in python 3.6 and above. It is a more readable and concise way to format strings.
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30