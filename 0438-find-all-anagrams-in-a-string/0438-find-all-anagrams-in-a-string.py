from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len: return []

        s_count, p_count, ans = defaultdict(int), defaultdict(int), []
        for i in range(p_len):
            p_count[p[i]] += 1
            s_count[s[i]] += 1
        if p_count == s_count: ans.append(0)

        left = 0
        for right in range(p_len, s_len):
            s_count[s[right]] += 1
            s_count[s[left]] -= 1

            if s_count[s[left]] == 0:
                s_count.pop(s[left])
            left += 1

            if s_count == p_count:
                ans.append(left)
        return ans

        
