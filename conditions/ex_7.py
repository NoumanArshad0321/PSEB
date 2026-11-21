bill = int(input("enter you bill:"))
discount=0
if bill >= 5000:
    discount=bill * 0.10
    print("discount:",discount,",","pay:",bill-discount)
elif bill<=4999 or bill==2000:
    discount=bill * 0.05
    print("discount:",discount,",","pay:",bill-discount)
else:
    print("None")
