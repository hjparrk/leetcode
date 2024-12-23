class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1, word2 = deque(word1), deque(word2)

        ans = ""
        while word1 and word2:
            ans += word1.popleft() + word2.popleft()
        
        if word1:
            ans += "".join(word1)
        if word2:
            ans += "".join(word2)
        
        return ans