class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        minimum = math.inf
        for i in range(1, len(arr)):
            diff = abs(arr[i]-arr[i-1])
            if diff==minimum:
                result.append([arr[i-1],arr[i]])
            if diff<minimum:
                minimum = diff
                result.clear()
                result.append([arr[i-1],arr[i]])
            
        return result