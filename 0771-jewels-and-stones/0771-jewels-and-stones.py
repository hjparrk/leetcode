from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        count = Counter(stones)
        for c in jewels:
            if c in count:
               ans += count[c]
        return ans