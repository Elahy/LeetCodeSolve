# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")
        
        def max_gain(node):
            nonlocal max_path
            
            if node is None:
                return 0
            
            gain_left = max(max_gain(node.left), 0)
            gain_right = max(max_gain(node.right), 0)
            
            curr_max = node.val + gain_left + gain_right
            
            max_path = max(curr_max, max_path)
            
            return node.val + max(gain_left, gain_right)
        
        max_gain(root)
        return max_path
        