class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        m = {}
        left = 0
        for right in range(len(s)):
            if s[right] in m:
                left = max(m[s[right]], left)

            ans = max(ans, right - left + 1)
            m[s[right]] = right + 1

        return ans
                
            
            