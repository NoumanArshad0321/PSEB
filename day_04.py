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


# updating a list and observing the effect on another variable referencing the same list
a = [1,2,3,4,5]
b=a
a[0]=100
print (b)


# city = "Lahore"
# city[0]="L"
# print(city)  # This will raise an error because strings are immutable in Python.
# it gives an error as we are trying to change the value of a string at a specific index, which is not allowed in Python since strings are immutable.



city = "Lahore"
print(id(city))  # This will print the memory address of the string object


city = city + " is a beautiful city."
print(id(city))  # This will print a different memory address, indicating that a new string object was created.


print("division:", 10 / 3)  

print("floor division:", 10 // 3)  

print(0.1+0.2)



from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))


# Random module

import random
random_number = random.randint(1, 100)  # Generate a random integer between 1 and 100
print("Random Number:", random_number)


teams=["Team A", "Team B", "Team C", "Team D"]
random_team = random.choice(teams)  # Randomly select a team from the list
print("Randomly Selected Team:", random_team)



import math

print("Square root of 16:", math.sqrt(16))
print("Ceiling of 3.2:", math.ceil(3.2))
print("Floor of 3.2:", math.floor(3.2))
print("Factorial of 5:", math.factorial(5))