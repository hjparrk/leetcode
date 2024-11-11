class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        dp = set([0])
        for num in nums:
            if num == target: return True
            if num > target: return False

            updated = set(dp)
            for elem in dp:
                updated.add(elem + num)
            dp = updated
        return False


