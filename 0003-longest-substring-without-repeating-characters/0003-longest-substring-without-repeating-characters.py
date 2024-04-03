class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         ans = 0
#         m = {}
#         left = 0
#         for right in range(len(s)):
#             if s[right] in m:
#                 left = max(m[s[right]], left)

#             ans = max(ans, right - left + 1)
#             m[s[right]] = right + 1

#         return ans
        
        ans = 0
        sub = ''
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                cut = sub.index(char)
                sub = sub[cut+1:] + char
        return ans
            
            