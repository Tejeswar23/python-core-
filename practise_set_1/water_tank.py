N = int(input("Enter: "))
inflows = list(map(int, input().split()))
capacity = 1000
current_volume = 0
overflow_minute = -1
for i in range(N):
    current_volume += inflows[i]

    if current_volume > capacity:
        overflow_minute = i + 1
        break

print(overflow_minute)
