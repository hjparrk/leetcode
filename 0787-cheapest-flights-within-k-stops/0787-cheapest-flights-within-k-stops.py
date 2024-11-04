from collections import defaultdict
from math import inf
from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for x, y, weight in flights:
            graph[x].append((y, weight))

        seen = {}
        heap = [(0, 0, src)] # price, stops, node
        while heap:
            price, stops, node = heappop(heap)
            seen[node] = stops

            if node == dst:
                return price
            
            if stops > k:
                continue
            
            for neighbor, neighbor_price in graph[node]:
                if neighbor in seen and seen[neighbor] <= stops:
                    continue
                new_price = price + neighbor_price
                heappush(heap, (new_price, stops + 1, neighbor))
        return -1