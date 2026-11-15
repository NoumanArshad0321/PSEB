print("***************************************** Question 1 *****************************************")
# Shopping Cart Example

shopping_cart = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
# for appending a new value to the list
append_result = shopping_cart.append("mango")  
print("After appending 'mango' to the shopping cart:", shopping_cart) 
# insert at 1
shopping_cart.insert(1, "nectarine")  
print("After inserting 'nectarine' at index 1:", shopping_cart)  

# removing a specific value from the list
shopping_cart.remove("banana")
print("After removing 'banana' from the shopping cart:", shopping_cart)  

# popping the last value from the list
popped_item = shopping_cart.pop()
print("After popping the last item from the shopping cart:", shopping_cart)
print("Popped item:", popped_item)



print("***************************************** Question 2 *****************************************")
# Copy or not

a=[1, 2, 3, 4, 5]
b=a
c=a.copy()
print("List a:", a)
print("List b:", b)
print("List c:", c)

a=[10, 20, 30]
print("After modifying list a:", a)
print("List b:", b)
print("List c:", c)


print("***************************************** Question 3 *****************************************")

print("***************************************** Table of 7 *****************************************")
numbers = list(range(1, 71))

print(numbers)
print("Table of 7:", numbers[6:71:7])  




print("***************************************** Question 4 *****************************************")
print("***************************************** Student Records *****************************************")

student_records=(("John Doe", 1, 90),("Jane Smith", 2, 85),("Alice Johnson", 3, 95),("Bob Brown", 4, 80),("Charlie Davis", 5, 88))
# for unpacking the tuple of student records
first_student_name, first_student_id, first_student_score = student_records[0]
print("First Student details are following below:")
print(f"Name: {first_student_name}")
print(f"ID: {first_student_id}")
print(f"Score: {first_student_score}")
