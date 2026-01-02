def binary_search(arr,target):
    l = 0
    r = len(arr)-1
    while(l <= r):
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target :
            l = mid + 1
        else:
            r = mid - 1
    return "No element found"
arr=[2,3,4,5,6,7,8]
target = 6
print("Found at Index :",binary_search(arr,target))