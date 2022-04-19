class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(v):
            if v == destination:
                return True
            unvisited[v] = 0
            for nb in adjlist[v]:
                if unvisited[nb]:
                    if dfs(nb):
                        return True
            return False
            
        adjlist = {}
        unvisited = [1]*n
        for i,j in edges:
            if i in adjlist:
                adjlist[i].append(j) 
            else: 
                adjlist[i] = [j]
            if j in adjlist:
                adjlist[j].append(i) 
            else:
                adjlist[j] = [i]
            
        return dfs(source)