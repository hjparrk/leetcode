from heapq import *

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []
        for num in arr:
            heappush(heap, (-abs(num - x), -num))
            if len(heap) > k:
                heappop(heap)
        return sorted([-num for _, num in heap])
