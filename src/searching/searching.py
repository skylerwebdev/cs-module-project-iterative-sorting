def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #check for empty array
    if len(arr) == 0:
        return -1
    l = 0
    h = len(arr)-1
    while h > l:
        m = (l+h) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            h = m
        elif arr[m] < target:
            l = m + 1

    return -1  # not found
