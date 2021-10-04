class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            n = len(arr)
            i = 0
            j = n - 1
            while i + 1 < n and arr[i] < arr[i + 1]:
                i += 1
            while j > 0 and arr[j - 1] > arr[j]:
                j -= 1
            return 0 < i == j < n - 1
            
        