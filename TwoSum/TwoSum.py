def twoSum(nums, target):
    numsIdx = {}
    for idx in range(len(nums)):
        potentialDiff = target - nums[idx]
        if potentialDiff in numsIdx:
            return [numsIdx[potentialDiff], idx]
        numsIdx[nums[idx]] = idx
    return []

print(twoSum([2,7,11,15],9))