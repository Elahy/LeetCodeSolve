class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        province = n
        parent = [0]*n
        rank = [0]*n
        
        for i in range(n):
            parent[i] = i
        
        def parentFinder(root):
            while(parent[root] != root):
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root
                
        def union(node1,node2):
            root1 = parentFinder(node1)
            root2 = parentFinder(node2)
            
            if(root1==root2): return 0
            
            if(rank[root1]>=rank[root2]):
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
            return 1
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    province -= union(i,j)
        return province