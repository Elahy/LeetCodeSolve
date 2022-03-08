class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        root = {}
        connected = {}
        result = 0
        
        for x in nums:
            root[x] = x
        for num in nums:
            if num-1 in root:
                root[num] = num-1
            
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return root[x]
        
        for num in nums:
            numRoot = find(num)
            if numRoot in connected:
                connected[numRoot].add(num)
            else:
                connected[numRoot] = set([num])
                
        for key in connected:
            result = max(result, len(connected[key]))
                         
        return result
        