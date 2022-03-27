class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        check = 0
        
        for i in range(0,n-1):
            
            if (i-count)%2 == 0:
                check+=1
                print(i,count)
                if nums[i] == nums[i+1]:
                    count += 1
                
        if n%2 == 0:
            return count if count%2 == 0 else count+1
        else:
            return count+1 if count%2 == 0 else count