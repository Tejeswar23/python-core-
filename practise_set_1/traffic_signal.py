time = int(input("Enter the time: "))
new_time = time % 90
if new_time == 0:
    new_time = 90
if new_time >= 1 and new_time <= 30:
    print("RED")
elif new_time >= 31 and new_time <= 45:
    print("YELLOW")
else:
    print("GREEN")

