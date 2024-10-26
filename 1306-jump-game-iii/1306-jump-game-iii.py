from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)
        def neighbors(node):
            nodes = []
            if node + arr[node] < length:
                nodes.append(node + arr[node])
            if 0 <= node - arr[node]:
                nodes.append(node - arr[node])
            return nodes

        seen = {start}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return False
        