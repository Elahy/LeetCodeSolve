class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[len(nums)-1] >= nums[0]: return nums[0]
        mini, start, end = nums[0], 0, len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            mini = min(mini,nums[mid])
            if nums[mid]>=nums[0]: start = mid+1
            else: end = mid-1
        return mini