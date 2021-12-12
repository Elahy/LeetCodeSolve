class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if (len(nums) == 1):
            return [nums[:]]
        
        
        for i in range(len(nums)):
            n = nums.pop(0)
            parms = self.permute(nums)
            
            for x in parms:
                x.append(n)
                
            result.extend(parms)
            nums.append(n)
            
        return result