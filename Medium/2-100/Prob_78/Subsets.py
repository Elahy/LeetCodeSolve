class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generateSubset(i,sub):
            if i == len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            generateSubset(i+1,sub)
            sub.pop()
            generateSubset(i+1,sub)
        res = []
        generateSubset(0,[])
        return res;