from collections import Counter
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        heap = []
        
        for num, frequency in counts.items():
            heappush(heap, (frequency, num))
            if len(heap) > k:
                heappop(heap)
        return [num for _, num in heap]
        