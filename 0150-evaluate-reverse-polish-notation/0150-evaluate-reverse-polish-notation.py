class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second, first = int(stack.pop()), int(stack.pop())
                if token == "+":
                    calculated = first + second
                if token == "-":
                    calculated = first - second
                if token == "*":
                    calculated = first * second
                if token == "/":
                    calculated = trunc(first / second)
                stack.append(calculated)
            else:
                stack.append(int(token))
        return stack.pop()