class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        dp = set([0])
        for num in nums: # O(n) times
            if num == target: return True
            if num > target: return False

            dp.update([sum + num for sum in dp]) # O(sum(nums))
            if target in dp: return True
        return False