from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        count = Counter(text)
        return min(count['a'],count['n'],count['b'],count['l']//2,count['o']//2)
        