def binarySearch(array, target):
    return CalculatebinarySearch(array, target, 0, len(array)-1)

def CalculatebinarySearch(array, target, left, right):
    while left <= right:
        middleIdx = (left + right) // 2
        potentialMatch = array[middleIdx]
        if target == potentialMatch:
            return middleIdx
        elif target < potentialMatch:
            right = middleIdx -1
        else:
            left = middleIdx + 1
    return -1

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 3))