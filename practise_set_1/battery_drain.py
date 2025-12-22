drain = int(input("Enter the drain rate: "))
battery = 100
min = 0
while battery > 0:
    battery = battery - drain
    min = min + 1
print(min)
