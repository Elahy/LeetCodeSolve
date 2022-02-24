class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        answer = [1]*len(nums)
        
        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]
            
        product = 1
        
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= product
            product *= nums[i]
            
        return answer