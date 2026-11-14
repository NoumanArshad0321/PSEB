# for the boolean 
from django.db.migrations import operations


print(True + True)  # Output: 2
print(True + False)  # Output: 1

print("python"[::-1])  # Output: nohtyp



first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print("Full Name:", full_name)  # Output: John Doe


print('hello \n '*10)




# operator precedence 
print(2 + 3 * 4)  # Output: 14 (multiplication has higher precedence than addition)
print((2 + 3) * 4)  # Output: 20 
print (2**3**2)



print(True and False)  # Output: False
print(True or False)   # Output: True


print(not True)  # Output: False



print(5 > 3)  # Output: True
print(5 < 3)  # Output: False
print(5 == 3)  # Output: False



print(sum([True, False, True]))  # Output: 2 (True is treated as 1, False as 0)



# Number System

print("Binary of 10:", bin(10))  # Output: 0b1010
print("Octal of 10:", oct(10))    # Output: 0o12
print("Hexadecimal of 10:", hex(10))  # Output: 0xa


print(int("1010", 2))  # Output: 10 (binary to decimal)
print(int("12", 8))    # Output: 10 (octal to decimal)
print(int("a", 16))    # Output: 10 (hexadecimal to decimal)

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a|b)
print(a&b)
print(a-b)
print(a^b)



name = "Alice"

print(name[::-1])

print("Pakistan"[2:6])  # Output: kist