class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        graph=defaultdict(list)
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
        Q=[]
        for i in graph:
            if len(graph[i])==1:
                Q.append(i)
        remain=n
        while remain>2:
            remain-=len(Q)
            new_Q=[]
            while Q:
                curr_leaf=Q.pop()
                adj=graph[curr_leaf].pop()#since curr_leaf in Q, it' length must be one, so pop will return the only node that connect with curr_leaf
                graph[adj].remove(curr_leaf)#remove the connection between curr_leaf and adj (mutual)
                if len(graph[adj])==1:
                    new_Q.append(adj)
                    
            Q=new_Q
        return Q
