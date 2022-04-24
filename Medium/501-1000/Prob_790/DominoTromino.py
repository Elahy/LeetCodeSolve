class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        oneold = 5
        twoold = 2
        threeold = 1
        result = 0
        for i in range(4,n+1):
            result = (oneold*2)+threeold
            threeold = twoold
            twoold = oneold
            oneold = result
        return result%1000000007