number = int(input("Enter a number: "))
if(number > 0 and number <= 31):
    for i in range(1,number+1):
        print(f"2^{i} = {2**i}")
else:
    print("Enter a valid number...")
