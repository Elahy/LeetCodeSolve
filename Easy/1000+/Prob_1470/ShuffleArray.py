class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array = [nums[0],nums[n]]
        lo, hi = 1, n+1
        while(lo<n):
            array.append(nums[lo])
            lo += 1
            array.append(nums[hi])
            hi += 1
        return array
        