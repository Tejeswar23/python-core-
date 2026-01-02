def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "No element found"
arr=[10,20,30,40,50]
target = 30
print("Found at Index :",linear_search(arr,target))