from heapq import *

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        heap, ans, cur = [], 0, 0 # heap (end time, profit so far)
        for start, end, prof in jobs:
            while heap and heap[0][0] <= start:
                end_time, prof_so_far = heappop(heap)
                cur = max(cur, prof_so_far)
            heappush(heap, (end, cur + prof))
            ans = max(ans, cur + prof)
        return ans