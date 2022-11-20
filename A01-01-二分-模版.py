
def binarySearch(a, target):
    left = 0
    right = len(a) - 1
    while(left <= right):
        mid = left  + (right - left) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # (right, left)