from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        half = n / 2
        counts = Counter(arr)
        occurences = sorted(counts.values())
        ans = 0
        for _ in range(len(occurences)):
            nums = occurences.pop()
            n -= nums
            if n <= half:
                return ans + 1
            ans += 1
        return ans
        