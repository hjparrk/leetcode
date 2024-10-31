class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def backtrack(num):
            if num >= 10 ** (n-1):
                ans.append(num)
                return
            
            prev = num % 10
            if k == 0:
                return backtrack(num * 10 + prev)
            if prev + k < 10:
                backtrack(num * 10 + prev + k)
            if prev - k >= 0:
                backtrack(num * 10 + prev - k)
    
        ans = []
        for i in range(1, 10):
            backtrack(i)
        return ans