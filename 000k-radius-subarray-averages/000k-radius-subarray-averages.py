class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        answer = [-1] * len(nums)
        for i in range(k, len(nums)-k):
            if i - k == 0:
                answer[i] = prefix[i+k] // (2*k+1)
            else:
                answer[i] = (prefix[i+k] - prefix[i-k-1]) // (2*k+1)
        
        return answer
        
        
        