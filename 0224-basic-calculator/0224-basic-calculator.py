class Solution:
    def calculate(self, s: str) -> int:

        ans, cur, sign, stack = 0, 0, 1, []
        for char in s:

            if char.isdigit():
                cur = cur * 10 + int(char)
            
            elif char in "+-":
                ans += sign * cur
                sign = 1 if char == "+" else -1
                cur = 0
            
            elif char == "(":
                stack.append(ans)
                stack.append(sign)

                sign = 1
                ans = 0
            
            elif char == ")":
                ans += sign * cur
                ans = (ans * stack.pop()) + stack.pop() # pop sign then prev num
                cur = 0

        return ans + (sign * cur)