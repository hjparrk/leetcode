from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(x, y):
            return (x ** 2 + y ** 2)

        heap = []
        for point in points:
            distance = get_distance(point[0], point[1])
            heappush(heap, (-distance, point))
            if len(heap) > k:
                heappop(heap)
        return [point for _, point in heap]
        