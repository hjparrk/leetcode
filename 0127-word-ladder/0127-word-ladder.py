from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        combinations = defaultdict(list)
        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                x = word[:i] + "_" +word[i+1:]
                combinations[x].append(word)

        seen = {beginWord}
        queue = deque([(beginWord, 1)]) # node, steps
        while queue:
            node, steps = queue.popleft()
            for i in range(length):
                x = node[:i] + "_" + node[i+1:]
                for word in combinations[x]:
                    if word == endWord:
                        return steps + 1
                    if word not in seen:
                        seen.add(word)
                        queue.append((word, steps + 1))
                combinations[x] = []
        return 0