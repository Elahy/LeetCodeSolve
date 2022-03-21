class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        res = []
        pacific, atlantic = set(), set()
        
        def dfs(i,j,prev,ocean):
            if i<0 or i>=row or j<0 or j>=col or heights[i][j]<prev or (i,j) in ocean:
                return
            ocean.add((i,j))
            dfs(i+1,j,heights[i][j],ocean)
            dfs(i-1,j,heights[i][j],ocean)
            dfs(i,j+1,heights[i][j],ocean)
            dfs(i,j-1,heights[i][j],ocean)
        
        for j in range(col):
            dfs(0,j,heights[0][j],pacific)
            dfs(row-1,j,heights[row-1][j],atlantic)
        for i in range(row):
            dfs(i,0,heights[i][0],pacific)
            dfs(i,col-1,heights[i][col-1],atlantic)
            
        for i,j in pacific:
            if (i,j) in atlantic:
                res.append([i,j])
                
        return res
        