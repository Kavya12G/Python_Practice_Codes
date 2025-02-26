def maxabsSubarr(nums):
    sum = 0
    minSum = 0
    maxSum = 0
    for num in nums:
        sum += num
        maxSum = max(sum, maxSum)
        minSum = min(sum, minSum)
    return abs(maxSum - minSum)

nums = list(map(int, input("Enter space seperated numbers: ").split()))
print(maxabsSubarr(nums))
