class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1]*(n+1)
        result = []
        for i in nums:
                arr[i] = 0
        for i in range(1,n+1):
            if arr[i] == 1:
                result.append(i)
        return result
        