class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        seen_at = dict()
        seen_at[0] = -1

        ans = curr = 0
        for i, num in enumerate(nums):
            curr += (num * 2 - 1) # 1 or -1
            if curr in seen_at: ans = max(ans, i - seen_at[curr])
            else: seen_at[curr] = i
        return ans