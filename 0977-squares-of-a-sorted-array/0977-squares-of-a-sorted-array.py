class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left, right = 0, n - 1

        for i in range(n - 1, -1, -1):
            left_num, right_num = abs(nums[left]) ,abs(nums[right])
            if right_num > left_num:
                ans[i] = pow(right_num, 2)
                right -= 1
            else:
                ans[i] = pow(left_num, 2)
                left += 1
        
        return ans

        