class Solution:
    def minStartValue(self, nums: List[int]) -> int:
            
        min_val = prefix_sum = 0 
        for num in nums:
            prefix_sum += num
            if prefix_sum < min_val:
                min_val = prefix_sum
        
        return -min_val + 1