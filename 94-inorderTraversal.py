class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        
        tree_vals = []
        def inorder(tree):

            if tree:

                inorder(tree.left)
                tree_vals.append(tree.val)
                inorder(tree.right)

        inorder(root)
        return tree_vals