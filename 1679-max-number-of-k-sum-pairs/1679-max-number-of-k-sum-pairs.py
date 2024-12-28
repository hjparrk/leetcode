from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans, mapping = 0, defaultdict(int)
        for num in nums:
            if mapping[num]:
                mapping[num] -= 1
                ans += 1
            else:
                mapping[k - num] += 1
        return ans