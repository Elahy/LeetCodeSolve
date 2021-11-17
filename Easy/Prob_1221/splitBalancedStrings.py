class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R = 0
        L = 0
        result = 0
        
        for i in s:
            if i == "R":
                R += 1
            else:
                L += 1

            if(R > 0 and R == L):
                result +=1
                R = 0
                L = 0
        return result
                