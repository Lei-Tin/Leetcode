# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        # If we have found p or q, return
        if root is p or root is q:
            return root

        search_left = self.lowestCommonAncestor(root.left, p, q)
        search_right = self.lowestCommonAncestor(root.right, p, q)

        # If we found p in the left and q in the right, return root
        # The other way around also works
        if search_left is not None and search_right is not None:
            return root

        else:
            # This means if we only found p or q in one of the branches, then that branch must be the lowest ancestor
            # Like, the location of p or q that we found must be the lowest ancestor
            if search_left is not None:
                return search_left
            if search_right is not None:
                return search_right

            return None
