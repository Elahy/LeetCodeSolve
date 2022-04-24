class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dicto = {}
        
        for i in nums:
            if i in dicto:
                dicto.pop(i)
            else:
                dicto[i] = "A"
        return list(dicto.keys())[0]
        