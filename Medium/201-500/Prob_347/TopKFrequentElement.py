class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checker = {}
        
        for num in nums:
            if num in checker:
                checker[num] += 1
            else:
                checker[num] = 1
        
        frequent = {}
        
        for key,val in checker.items():
            if val in frequent:
                frequent[val].append(key)
            else:
                frequent[val] = [key]
                
        res = []
        
        for i in range(len(nums),0,-1):
            if i in frequent:
                res += frequent[i]
        
        return res[:k]