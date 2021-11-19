class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        result = 0
        
        while xor != 0:
            if (xor & 1):
                result += 1
            xor = xor // 2
        
        return result
        