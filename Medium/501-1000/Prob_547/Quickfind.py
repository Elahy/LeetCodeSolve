class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected[0])
        root = [0]*n
        provinces = n
        
        for i in range(n):
            root[i] = i
        
        def union(x,y):
            rootX = root[x]
            rootY = root[y]
            if rootX != rootY:
                for i in range(n):
                    if root[i] == rootY:
                        root[i] = rootX
                return -1
            return 0
            
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    provinces += union(i,j)

        return provinces