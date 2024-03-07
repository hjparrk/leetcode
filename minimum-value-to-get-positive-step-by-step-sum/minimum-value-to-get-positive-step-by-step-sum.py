class Solution:
    def minStartValue(self, nums: List[int]) -> int:
            
        min_val = curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            min_val = curr if curr < min_val else min_val

        return -min_val + 1