class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sums, i = 0, 1
        nums.sort()
        while i < len(nums):
            sums += min(nums[i-1], nums[i])
            i += 2
        return sums
        