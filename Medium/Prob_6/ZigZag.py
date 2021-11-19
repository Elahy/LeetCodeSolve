class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows != 1:
            arr = [""]*numRows
            row = 0
            step = 1
            
            for i in s:
                arr[row] += i
                
                if row == 0:
                    step = 1
                elif row == (numRows -1):
                    step = -1
                
                row += step
            
            s = ""  
            for i in arr:
                s += i 
            return s
        else:
            return s