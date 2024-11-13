class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = ""
        for i in range(len(s)):
            # odd
            left, right = i, i
            while 0 <= left and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1
            
            # # even
            left, right = i, i + 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1
        return ans
