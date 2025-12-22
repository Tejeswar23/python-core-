balance = int(input("Enter the Balance: "))
n = int(input("Enter number of transactions: "))
for i in range(n):
    amount = int(input("Enter the amount: "))
    if amount % 100 == 0 and amount <= balance:
        balance = balance - amount
        print("SUCCESS")
    else:
        print("FAILED")
print(balance)

