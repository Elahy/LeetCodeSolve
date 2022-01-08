class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxProd = 1
        minProd = 1
        best = 0
        
        for i in nums:
            if i < 0:
                maxProd, minProd = minProd, maxProd
            maxProd = max(maxProd*i, i)
            minProd = min(minProd*i, i)
            best = max(maxProd, best)
            
        return best