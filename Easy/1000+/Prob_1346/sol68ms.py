class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h = set()
        for i in arr:
            if 2*i in h or i/2 in h:
                return True
            else:
                h.add(i)
        return False