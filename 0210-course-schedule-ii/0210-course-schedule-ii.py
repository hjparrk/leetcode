from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indegrees = defaultdict(list), [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
        
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            if len(ans) == numCourses:
                return ans

            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return []