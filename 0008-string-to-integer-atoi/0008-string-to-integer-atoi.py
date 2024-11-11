from collections import deque

class Solution:
    def myAtoi(self, s: str) -> int:
        nums = set([str(num) for num in range(10)])
        signs = set(["-", "+"])
        num_found, is_negative = False, False
        queue = deque()
        for letter in s.strip():
            if not num_found and letter == "-":
                is_negative = True
            elif not num_found and letter == "+":
                continue
            elif letter in nums:
                num_found = True
                queue.append(letter)
            else:
                break
        
        ans = 0
        MAX, MIN = 2**31 - 1, -2**31
        while queue:
            popped = queue.popleft()
            ans = (ans * 10) + int(popped)
        ans = ans if not is_negative else -ans
        if ans > MAX:
            ans = MAX
        if ans < MIN:
            ans = MIN
        return ans