from collections import defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        # graph = defaultdict(list)
        # for x, y in redEdges:
        #     graph[x].append((y, "red"))
        # for x, y in blueEdges:
        #     graph[x].append((y, "blue"))

        # ans = [-1] * n
        # ans[0] = 0
        # seen = {(0, None)}
        # queue = deque([(0, None, 0)]) # node, previous color, steps
        
        # while queue:
        #     node, prev_color, steps = queue.popleft()
        #     for neighbor, color in graph[node]:
        #         if prev_color != color and (neighbor, color) not in seen:
        #             seen.add((neighbor, color))
        #             queue.append((neighbor, color, steps + 1))
        #             if neighbor != 0:
        #                 ans[neighbor] = steps + 1
        # return ans

        RED = 0
        BLUE = 1
        
        graph = defaultdict(lambda: defaultdict(list))
        for x, y in redEdges:
            graph[RED][x].append(y)
        for x, y in blueEdges:
            graph[BLUE][x].append(y)
        
        ans = [float("inf")] * n
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        seen = {(0, RED), (0, BLUE)}
        
        while queue:
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)
            
            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor, 1 - color))
                    queue.append((neighbor, 1 - color, steps + 1))
        
        return [x if x != float("inf") else -1 for x in ans]
        