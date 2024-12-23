class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        if str1 + str2 != str2 + str1:
            return ""

        gcd = gcd(len(str1), len(str2))
        return str1[:gcd]