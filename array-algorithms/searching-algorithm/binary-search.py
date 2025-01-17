def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        print(low)
        print(high)
        mid = (low + high) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
print(binary_search(arr, target))
