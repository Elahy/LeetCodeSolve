class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        res = []
        unvisited = [True]*numCourses
        helper = [True]*numCourses
        
        for [child, root] in prerequisites:
            adj[root].append(child)
            
        def checkCycle(i):
            unvisited[i] = False
            helper[i] = False
            for node in adj[i]:
                if unvisited[node]:
                    if checkCycle(node):
                        return True
                if helper[node] == False:
                    return True
            helper[i] = True
        for i in range(numCourses):
            if unvisited[i]:
                if checkCycle(i):
                    return res
                
        inDegree = [0]*numCourses
        for i in range(numCourses):
            for node in adj[i]:
                inDegree[node] += 1
        queue = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        while(queue):
            node = queue.pop(0)
            res.append(node)
            for neib in adj[node]:
                inDegree[neib] -= 1
                if inDegree[neib] == 0:
                    queue.append(neib)
        return res