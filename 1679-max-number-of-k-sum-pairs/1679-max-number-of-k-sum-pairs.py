from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans, mapping = 0, defaultdict(list)
        for num in nums:
            if mapping[num]:
                mapping[num].pop()
                ans += 1
            else:
                mapping[k - num].append(num)
        return ans