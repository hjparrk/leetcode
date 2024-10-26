from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        if not bank:
            return -1
        if endGene not in bank:
            return -1

        length = len(startGene)
        seen = {startGene}
        queue = deque([(startGene, 0)])
        while queue:
            node, steps = queue.popleft()
            if node == endGene:
                return steps
            for character in "ACGT":
                for i in range(length):
                    neighbor = node[:i] + character + node[i+1:]
                    if neighbor not in seen and neighbor in bank:
                        seen.add(neighbor)
                        queue.append((neighbor, steps + 1))
        return -1