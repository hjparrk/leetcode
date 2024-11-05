from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = Counter(nums)
        return max(counts, key = lambda x: counts[x])