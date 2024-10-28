class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = str(num)
        for i, digit in enumerate(ans):
            if int(digit) == 6:
                return int(ans[:i] + '9' + ans[i+1:])
        return int(ans)
        