class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        limit = 5000
        ans = 0
        for w in weight:
            if w <= limit:
                ans += 1
                limit -= w
            else:
                break
        return ans


        