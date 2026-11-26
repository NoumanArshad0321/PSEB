numbers = [12, 7, 9, 20, 33, 48, 51]
result={}
Even=0
Odd=0

for i in numbers:
    if i%2==0:
        Even+=1
        result["even"]=Even
    else:
        Odd+=1
        result["odd"]=Odd

print(result)