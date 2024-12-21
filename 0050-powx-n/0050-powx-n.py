class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0

        def helper(x, n):
            if n == 0: return 1

            ans = helper(x, n // 2)
            ans *= ans
            
            return x * ans if n % 2 else ans

        ans = helper(x , abs(n))
        return ans if n > 0 else 1 / ans