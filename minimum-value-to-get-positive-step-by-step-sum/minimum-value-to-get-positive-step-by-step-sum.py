class Solution:
    def minStartValue(self, nums: List[int]) -> int:
            
        sum = min_val = 0 
        for num in nums:
            sum += num
            min_val = min(min_val, sum)
        return -min_val + 1