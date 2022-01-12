class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        cur_color = image[sr][sc]
        
        def dfs(sr, sc):
            nonlocal rows, cols, newColor, image
            
            if sr < 0 or sc < 0 or sr>rows-1 or sc>cols-1 or image[sr][sc]==newColor or image[sr][sc]!=cur_color:
                return
            
            image[sr][sc] = newColor
            
            dfs(sr+1,sc)
            dfs(sr-1,sc)
            dfs(sr,sc+1)
            dfs(sr,sc-1)
        
        dfs(sr, sc)
        
        return image