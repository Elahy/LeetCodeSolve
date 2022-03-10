class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for i in range(numCourses)]
        visited = [0]*numCourses
        helper = [0]*numCourses
        
        for [child, root] in prerequisites:
            adjList[root].append(child)
        
        def detectCycle(v):
            visited[v] = 1
            helper[v] = 1
            
            for neighbour in adjList[v]:
                if visited[neighbour] != 1:
                    if detectCycle(neighbour):
                        return True
                if helper[neighbour]:
                    return True
            helper[v] = 0
            return False
        
        for i in range(numCourses):
            if visited[i] != 1:
                if detectCycle(i):
                    return False
        return True
        