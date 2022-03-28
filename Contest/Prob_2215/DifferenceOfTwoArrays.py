class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        nums1c, nums2c = {}, {}
        
        for i in nums1:
            if i not in nums1c:
                nums1c[i] = i
        for i in nums2:
            if i not in nums2c:
                nums2c[i] = i
        for key in nums1c:
            if key not in nums2c:
                answer[0].append(key)
        for key in nums2c:
            if key not in nums1c:
                answer[1].append(key)
        return answer
        
        