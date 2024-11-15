from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapify(max_heap)

        time = 0
        queue = deque() # -count, idle_time
        while max_heap or queue:
            time += 1
            if max_heap:
                count = 1 + heappop(max_heap)
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                heappush(max_heap, queue.popleft()[0])
        return time

        


        return 0