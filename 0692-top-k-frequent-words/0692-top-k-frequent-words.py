from collections import Counter
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        for word, freq in Counter(words).items():
            heappush(heap, (-freq, word))

        return [heappop(heap)[1] for _ in range(k)]
        # O((n + k) log n)