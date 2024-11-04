from re import sub

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = sub(r'[^a-zA-Z0-9]', '', s).lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True