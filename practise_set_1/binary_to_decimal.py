binary = input("Enter the Number: ")
decimal = 0
power = 0
i = len(binary) - 1
while i >= 0:
    if binary[i] == '1':
        decimal = decimal + (2 ** power)
    power += 1
    i -= 1
print(decimal)
