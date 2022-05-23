class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = [0]*len(nums)
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if i != j and nums[j]<nums[i]:
                    counter += 1
            smaller[i] = counter
        return smaller
        