class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for element in nums:
            if element == val:
                nums.remove(element)
                k +=1
        return k
            