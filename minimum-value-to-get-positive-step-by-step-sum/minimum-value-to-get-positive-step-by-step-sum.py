class Solution:
    def minStartValue(self, nums: List[int]) -> int:
            
        min_val = curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr < min_val:
                min_val = curr

        return -min_val + 1