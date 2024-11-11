class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        dp = set()
        dp.add(0)
        target = total_sum // 2
        for num in nums:
            next_dp = set()
            for elem in dp:
                next_dp.add(elem)
                next_dp.add(elem + num)
            dp = next_dp
        return True if target in dp else False


