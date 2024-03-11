class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1 = set(nums)
        set2 = { x for x in range(len(nums) + 1)}
        
        return (set2 - set1).pop()