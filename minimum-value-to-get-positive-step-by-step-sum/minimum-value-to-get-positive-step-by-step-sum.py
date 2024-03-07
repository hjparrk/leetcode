class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        min_val1 = 0
        total = 0

        for num in nums:
            total += num
            min_val1 = min(min_val1, total)
            
        min_val = curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr < min_val:
                min_val = curr
        
        print(min_val1)
        print(min_val)

        return -min_val + 1