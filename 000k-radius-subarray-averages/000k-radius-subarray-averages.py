class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
        
        ans = [-1] * n
        for i in range(k, n-k):
            ans[i] = (prefix[i+k] - prefix[i-k] + nums[i-k]) // (2*k+1)
        
        return ans
        
        
        