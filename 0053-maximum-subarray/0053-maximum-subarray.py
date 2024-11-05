class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total, ans = 0, float("-inf")
        for num in nums:
            if total < 0:
                total = 0

            total += num
            ans = max(ans, total)
        return ans