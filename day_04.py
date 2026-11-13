username = "Nouman"     
print("Hello, " + username + "! Welcome to the program.")

username = "Arshad"
print("Hello, " + username + "! Welcome to the program.")
# the username variable is reassigned to a new value, and the program prints a different greeting message.if i want to chng the index of the username it will throw erro as it is not mutable 


age = 10
print("Age:", age)

# int is also immutable 
age=11
print("Age:", age)


# Lists are mutable, meaning you can change their elements after creation. Here's an example:
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
fruits[1] = "orange"  # Changing the second element
print("Updated Fruits:", fruits)




# Dictionaries are mutable, meaning you can change their values after creation. Here's an example:
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Students:", students)
students["Alice"] = 88  # Updating Alice's grade
print("Updated Students:", students)