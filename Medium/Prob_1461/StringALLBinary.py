class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        lookup = set()
        for i in range(len(s)-k+1):
            lookup.add(s[i:i+k])
        return len(lookup) == 2**k