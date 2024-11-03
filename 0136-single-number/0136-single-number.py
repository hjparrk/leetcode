from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num, freq in counts.items():
            if freq < 2:
                return num
            
        