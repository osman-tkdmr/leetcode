# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findTarget(self, root, k):
        res=[]
        def helper(root,k):   
            if root:
                if k-root.val in res:return True
                res.append(root.val)
                
                return helper(root.left,k) or helper(root.right,k)
                
        c=helper(root,k)        
        if c:
            return True
        return False
        