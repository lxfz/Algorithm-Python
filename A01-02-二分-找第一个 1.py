from typing import List

def valid(x):
    if x == 0:
        return True
    
    # x == 1
    return False


def binarySearch(a:List[int]):
    """
    a: [0,0,0,...,0,1,1,1,1]
    """
    
    left = 0
    right = len(a) - 1
    while(left <= right):
        mid = left + (right - left) // 2
        if(valid(a[mid])):
            left = mid+1
        else:
            right = mid - 1
        
        return left
    # (right, left)