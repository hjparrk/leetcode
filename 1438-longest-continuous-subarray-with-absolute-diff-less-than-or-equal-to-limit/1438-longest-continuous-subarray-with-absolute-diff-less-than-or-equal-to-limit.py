from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        increasing, decreasing = deque(), deque()
        ans = left = 0

        for right, num in enumerate(nums):
            
            while increasing and increasing[-1] > num:
                increasing.pop()
            while decreasing and decreasing[-1] < num:
                decreasing.pop()

            increasing.append(num)
            decreasing.append(num)

            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans

