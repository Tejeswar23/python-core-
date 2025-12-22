import random
num = int(input("Enter the number: "))
if(num > 0):
    for i in range(1,num+1):
        flip=random.randint(0,1)
        heads=0
        tails=0
        if(flip == 0):
            heads+=1
        else:
            tails+=1
        head_per = (heads/num)*100
        tails_per = (tails/num)*100
    print(f"Heads:{head_per:.2f}%,Tails:{tails_per:.2f}%")
else:
    print("Enter a valid number...")
