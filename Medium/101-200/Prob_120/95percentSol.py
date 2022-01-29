class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        for i in range(rows-2,-1,-1):
            for j in range(0,i+1):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]