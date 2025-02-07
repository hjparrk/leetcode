class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        max_area = 0
        for i, cur_height in enumerate(heights):
            while stack and heights[stack[-1]] > cur_height:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, width * height)
            stack.append(i)
        return max_area