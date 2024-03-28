from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        ans = 0
        chars = set("balloon")
        count = Counter(text)
        
        # set 'AND' operation
        if len(chars & count.keys()) != 5:
            return ans
        
        ans = min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])
        return ans
        
        