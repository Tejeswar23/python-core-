num=int(input("Enter a number: "))
harmonic_value=0
if num>0:
    for i in range(1,num+1):
        harmonic_value+=1/i
    print(f"The harmonic value is: {harmonic_value}")
else:
    print("Enter a valid number...")
