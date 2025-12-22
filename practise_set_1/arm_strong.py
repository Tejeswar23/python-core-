num = input("Enter the number: ")
count = len(num)
real_num = int(num)
org_num = real_num
sum = 0
while(real_num > 0):
    rem = real_num%10
    sum += (rem**count)
    real_num = real_num//10
if sum == org_num :
    print("ArmStrong Number")
else:
    print("Not ArmStrong Number")
