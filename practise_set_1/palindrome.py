n = int(input("Enter the number: "))
org_n = n
ans = 0
while(n > 0):
    rem = n % 10
    ans = ans * 10 + rem
    n = n // 10
if org_n == ans:
    print("YES")
else:
    print("NO")
