class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target == matrix[0][0]:
            return True
        else:
            col = len(matrix[0])
            start = 0
            end = len(matrix)*col - 1
            while start <= end:
                mid = (start + end) // 2
                if target == matrix[mid // col][mid % col]:
                    return True
                elif target  <  matrix[mid // col][mid % col]:
                    end = mid - 1
                else:
                    start = mid + 1
            return False
                
            
        