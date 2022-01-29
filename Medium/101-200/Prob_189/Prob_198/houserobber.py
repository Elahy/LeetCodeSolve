class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b,i = 0,0,0
        
        for i in range(len(nums)):
            if i%2 == 0:
                a = max(a+nums[i], b)
            else:
                b = max(b+nums[i], a)
                
        return max(a,b)
        