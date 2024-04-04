class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        matches = {"(" : ")", "{" : "}", "[": "]"}

        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if not stack:
                    return False
                prev_opening = stack.pop()
                if matches[prev_opening] != c:
                    return False
        
        return not stack

        