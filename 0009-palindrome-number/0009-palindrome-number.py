class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        reversenum = 0
        y = x

        while x > 0:
            reminder = x%10
            reversenum = reversenum*10 + reminder
            x = x // 10

        if y == reversenum:
            return True
        else:
            return False            
        