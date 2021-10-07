class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p = len(nums1)
        q = len(nums2)
        r = p+q
        arr = []*r
        arr[0:p-1] = nums1
        arr[p:r-1] = nums2
        arr.sort()
        if(r%2 == 0):
            return (arr[r//2] + arr[(r//2)-1]) / 2
        else:
            return arr[(r//2)]
        