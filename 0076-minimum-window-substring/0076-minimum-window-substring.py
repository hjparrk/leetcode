from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == 0: return ""
        count = Counter(t)
        window = defaultdict(int)

        have, need = 0, len(t)
        ans, ans_len = [-1, -1], float('inf')

        left = 0
        for right in range(len(s)):
            char = s[right]

            window[char] += 1
            if char in count and window[char] <= count[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < ans_len:
                    ans = [left, right]
                    ans_len = (right - left + 1)
                
                window[s[left]] -= 1
                if s[left] in count and window[s[left]] < count[s[left]]:
                    have -= 1
                left += 1
        
        left, right = ans[0], ans[1]
        return s[left:right + 1] if ans_len != float('inf') else ""