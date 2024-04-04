class Solution:
    def removeDuplicates(self, s: str) -> str:

        ans = ""
        stack = []

        for c in s:
            if not stack or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()

        for _ in range(len(stack)):
            ans += stack.pop()

        return ans[::-1]

        

            