n = input("Enter the number: ")
bool = True
for i in range(len(n) - 1):
    if n[i] >= n[i + 1]:
        bool = False
        break
if bool:
    print("YES")
else:
    print("NO")
