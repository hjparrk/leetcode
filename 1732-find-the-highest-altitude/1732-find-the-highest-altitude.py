class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

            ans = curr = 0
            for value in gain:
                curr += value
                ans = max(ans, curr)
            return ans