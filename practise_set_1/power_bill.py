used_units = int(input("Enter the units: "))
bill = 0
if(used_units > 0 and used_units <= 100):
    bill = used_units*3
elif(used_units > 100 and used_units <= 200):
    bill = (100 * 3) + (used_units - 100) * 5
else:
    bill = (100 * 3) + (100 * 5) + (used_units - 200) * 8
if(used_units > 300):
    bill=bill+(bill*0.10)
print(int(bill))
