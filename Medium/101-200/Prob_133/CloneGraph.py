"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        
        def dfs(node):
            if node.val in visited:
                return visited[node.val]
            
            clone = Node()
            clone.val = node.val
            visited[node.val] = clone
            for item in node.neighbors:
                clone.neighbors.append(dfs(item))
                
            return clone

        
        return dfs(node)
        