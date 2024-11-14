class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return
            for letter in letters[digits[i]]:
                curr.append(letter)
                backtrack(curr, i + 1)
                curr.pop()
        
        ans = []
        backtrack([], 0)
        return ans
        