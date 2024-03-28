from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        m = {0:-1}
        counter = ans = 0
        for i, num in enumerate(nums):
            counter += (num*2 - 1)
            if counter in m: 
                ans = max(ans, i - m[counter])
            else: 
                m[counter] = i
        return ans
            
        
        