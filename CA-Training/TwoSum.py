def twoNumberSum(array, targetSum):
	count = {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in count:
			return [num, potentialMatch]
		count[num] = True
	return []

print(twoNumberSum([2,7,12,5], 9))