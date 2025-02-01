class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:  # Both even or both odd
                return False
        return True