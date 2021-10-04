class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits)-1
        if(digits[last]<9):
            digits[last] += 1
            return digits
        else:
            num = 0
            for i in range(len(digits)):
    	        num += digits[i] * pow(10, (len(digits)-1-i))
            return [int(i) for i in str(num+1)]

        