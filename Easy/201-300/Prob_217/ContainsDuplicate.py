class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Checker = set()
        for num in nums:
            if num in Checker:
                return True
            else:
                Checker.add(num)
        return False