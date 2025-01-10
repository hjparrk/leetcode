import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for x, y, price in flights:
            graph[x].append((y, price))

        steps = [float('inf')] * n
        steps[src] = 0

        heap = [(0, src, 0)] # price, node, step
        while heap:
            price, node, step = heappop(heap)

            if step > steps[node]:
                continue
            if step > k + 1:
                continue
            steps[node] = step
            
            if node == dst:
                return price

            for neighbor, neighbor_price in graph[node]:
                heappush(heap, (price + neighbor_price, neighbor, step + 1))
        
        return -1