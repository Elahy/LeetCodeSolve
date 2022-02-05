class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [0]*4
        i = 0;
        while num>0:
            digits[i] = num%10
            num //= 10
            i += 1
        digits.sort()
        return ((digits[0]*10)+digits[3]) + ((digits[1]*10)+digits[2])
        