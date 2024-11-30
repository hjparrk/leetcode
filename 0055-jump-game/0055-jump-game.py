class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached, n = 0, len(nums)
        for i in range(n):
            if i > reached:
                return False
            reached = max(reached, i + nums[i])
            if reached >= n - 1:
                return True
        return False