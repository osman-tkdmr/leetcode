# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        def ins(val, node, depth, n):
            if not node:
                return
            if depth == n-1:
                tmp = node.left
                node.left = TreeNode(val)
                node.left.left = tmp
                tmp = node.right
                node.right = TreeNode(val)
                node.right.right = tmp
            else:
                ins(val, node.left, depth+1 , n)
                ins(val, node.right, depth+1, n)
        if depth == 1 :
            n = TreeNode(val)
            n.left = root
            return n
        ins(val, root, 1, depth)
        return root
        