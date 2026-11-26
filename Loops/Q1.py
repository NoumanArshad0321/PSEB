marks = [78,45,92,33,67,88]
passed=0

for i in marks:
    if i >=40:
        passed+=1
        print(f"{i} Pass")
        
    else:
        print(f"{i} fail")    

print(f"Passed : {passed}")