class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x > 0 and x % 10 == 0):
            return False

        def reverse_num(num):
            reversed_number = 0
            while num != 0:
                digit = num % 10
                reversed_number = reversed_number * 10 + digit
                num = num // 10
            return reversed_number
        
        return True if x == reverse_num(x) else False