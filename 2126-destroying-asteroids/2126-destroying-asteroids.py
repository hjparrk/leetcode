from heapq import *

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heap = asteroids
        heapify(asteroids)

        while heap:
            if heap[0] > mass:
                return False
            mass += heappop(heap)
        return True

        