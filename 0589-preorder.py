
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        if root is None:
            return []
        
        res = [root.val] 
        for children in root.children:
            res.extend(self.preorder(children))
        
        return res