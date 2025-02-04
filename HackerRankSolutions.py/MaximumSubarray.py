class Solution:
    def maxAscendingSum(nums):
        max_sum = 0
        current_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current_sum+=nums[i]
            else:
                max_sum=max(max_sum, current_sum)
                current_sum=nums[i]
        return max(max_sum,current_sum)