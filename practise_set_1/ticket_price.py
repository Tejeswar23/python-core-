dist = int(input("Enter the distance: "))
age = int(input("Enter the age: "))
actual_price = dist*2
if age > 60 :
    actual_price = actual_price-(actual_price*30/100)
elif age<12 :
    actual_price = actual_price-(actual_price*50/100)
print(actual_price)
