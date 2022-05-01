# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        elif val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)

        else:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)

        return root

        # Solution 2
        # if root is None:
        #     return TreeNode(val)
        #
        # elif val > root.val:
        #     root.right = self.insertIntoBST(root.right, val)
        #
        # else:
        #     root.left = self.insertIntoBST(root.left, val)
        #
        # return root
