class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen.pop(i)
            else:
                seen[i] = "1"
        return seen
        