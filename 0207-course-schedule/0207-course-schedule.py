from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        seen = set()
        def dfs(node):
            if node in seen:
                return False
            
            if not graph[node]:
                return True
            
            seen.add(node)
            for course in graph[node]:
                if not dfs(course):
                    return False
            
            seen.remove(node)
            graph[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True