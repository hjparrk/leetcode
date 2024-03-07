class Solution:
    def minStartValue(self, nums: List[int]) -> int:
            
        min_val = prefix_sum = 0 
        for num in nums:
            prefix_sum += num
            min_val = min(min_val,prefix_sum)
        return abs(min_val) + 1