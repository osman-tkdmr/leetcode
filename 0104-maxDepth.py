# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        def helper(root,depth):
            if not root: return depth
            return max(helper(root.right, depth+1),helper(root.left, depth+1))
        return helper(root,0)
        