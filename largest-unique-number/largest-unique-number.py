from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        l = [k for k in count if count[k] == 1]
        return max(l) if len(l) else -1
                