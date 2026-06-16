print("First 100 units = Rs.5/unit")
print("Next 100 units = Rs.8/unit")
print("Above 200 units = Rs.10/unit")
units=int(input("Enter total units="))
if units<=100:
    charges=units*5
    print("charges=",charges)
elif units<=200:
    ch=100*5+(units-100)*8
    print("charges=",ch)
else:
    bill=100*5+(100*8)+((units-200)*10)
    print("charges=",bill)

    print("Total amount of electricity bill = ",bill) 