class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1

        left_max, right_max = 0, 0
        waters = 0
        while left < right:

            if height[left] < height[right]:
                if height[left] <= left_max:
                    waters += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1

            else:
                if height[right] <= right_max:
                    waters += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
                
        return waters