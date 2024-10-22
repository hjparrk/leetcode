class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
        
        
        dic = collections.defaultdict(list)
        for i, num in enumerate(nums):
            if target - num in dic:
                return [i, dic[target - num]]
            else:
                dic[num] = i
                