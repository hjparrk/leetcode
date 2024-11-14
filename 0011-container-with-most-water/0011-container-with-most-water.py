class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calc_area(left, right):
            return (right - left) * min(height[left], height[right])
        
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = calc_area(left, right)
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
