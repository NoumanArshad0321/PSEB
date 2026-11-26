table = int(input("Which table do you want to print: "))
start = int(input("Enter from where you want o start the table : "))
end = int(input("Enter the value on which you want to end the table: "))




while start<=end:
    print(f"{table} x {start} = {table*start}")
    start += 1



