class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        
        dp = set()
        dp.add(0)
        for num in nums:
            if num == target:
                return True
            if num > target:
                return False
            next_dp = set()
            for elem in dp:
                if elem + num == target:
                    return True
                next_dp.add(elem + num)
                next_dp.add(elem)
            dp = next_dp
        return False


