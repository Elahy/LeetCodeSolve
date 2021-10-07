class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum = 0
        n = 0
        temp = x
        while x > 0:
            n = x % 10
            sum = (sum*10)+n
            x = x//10
        if sum == temp:
            return True
        else:
            return False