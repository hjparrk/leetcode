class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(s)

        left = 0
        right = len(s) - 1

        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp

            left += 1
            right -= 1

        print(s)
        