class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        ans = curr = 0
        for i, char in enumerate(s):
            if i >= k and s[i - k] in vowels:
                curr -= 1
            if char in vowels:
                curr += 1
            ans = max(ans, curr)
        return ans
