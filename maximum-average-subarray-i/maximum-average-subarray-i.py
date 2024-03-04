class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        answer = curr = sum(nums[:k])
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            
            answer = max(answer, curr)
        
        return answer / k