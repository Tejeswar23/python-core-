n = int(input("Enter the number: "))
while(n > 10):
    s = 0
    while(n > 0):
        s = s + (n % 10)
        n = n // 10
    n = s
print(n)
