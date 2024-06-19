class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        left, right = 0, len(nums) - 1

        for _ in range(len(nums)):
            left_num, right_num = abs(nums[left]) ,abs(nums[right])
            if right_num > left_num:
                ans.insert(0, pow(right_num, 2))
                right -= 1
            else:
                ans.insert(0, pow(left_num, 2))
                left += 1
        
        return ans

        