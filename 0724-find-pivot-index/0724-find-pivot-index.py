class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        for i in range(1, len(prefix)):
            if prefix[i - 1] == prefix[n] - prefix[i]:
                return i - 1
        return -1