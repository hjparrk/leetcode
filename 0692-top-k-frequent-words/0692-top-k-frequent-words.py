from collections import Counter
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = Counter(words)

        heap = []
        for word, freq in frequencies.items():
            heappush(heap, (-freq, word))

        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
        return ans