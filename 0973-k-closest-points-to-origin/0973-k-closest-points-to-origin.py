from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for point in points:
            distance = (point[0] ** 2) + (point[1] ** 2)
            heappush(heap, (-distance, point))
            if len(heap) > k:
                heappop(heap)
        return [point for _, point in heap]