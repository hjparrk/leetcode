class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        ans = ""
        for i in range(len(s)):
            # odd
            left, right = i, i
            odd = expand(left, right)
            ans = odd if len(odd) > len(ans) else ans
            
            # even
            left, right = i, i + 1
            even = expand(left, right)
            ans = even if len(even) > len(ans) else ans

        return ans