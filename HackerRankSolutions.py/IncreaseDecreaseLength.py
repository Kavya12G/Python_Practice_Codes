class Solution:
    def longestMonotonicSubarray(nums):
        if not nums:
           return 0

        enc = 1 
        dec = 1
        max_len = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                enc+=1
                dec = 1
            elif(nums[i] < nums[i-1]):
                dec+=1
                enc = 1
            else:
                enc = dec = 1
            max_len = max(max_len, enc, dec)
        return max_len