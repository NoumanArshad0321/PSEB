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




# Arithmetic Operations
x = 10  
y = 5
z = x + y  # Addition
print("Sum:", z)

# Subtraction
z = x - y
print("Difference:", z)

# Multiplication
z = x * y
print("Product:", z)

# Division
z = x / y
print("Quotient:", z)



print("reminder:", x % y)  # Modulus


print("Exponentiation:", x ** y)  # Exponentiation





# Type Conversion
num_str = "42"
num_int = int(num_str)  # Convert string to integer
print("Converted Integer:", num_int)
print



# convert integer to string
num_int = 42        
num_str = str(num_int)  
print("Converted String:", num_str)
print("Type of num_str:", type(num_str))  # Output: <class 'str'>


# convert float to integer
num_float = 3.14
num_int = int(num_float) 
print("Converted Integer from Float:", num_int)
print("Type of num_int:", type(num_int))  # Output: <class 'int'>