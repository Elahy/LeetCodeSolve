class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeroes = arr.count(0)
        extended = n + zeroes
        
        i = n -1
        j = extended - 1
        
        while j >= 0:
            if j < n:
                arr[j] = arr[i]
            j-=1
            if arr[i] == 0:
                if j < n:
                    arr[j] = arr[i]
                j -= 1
            i-=1