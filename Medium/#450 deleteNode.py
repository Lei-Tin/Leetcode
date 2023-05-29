# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # The case where we found the item
            if root.right is None:
                return root.left

            if root.left is None:
                return root.right

            if root.left is not None and root.right is not None:
                # Find the sucessor of the current node and replace itself with it
                right = root.right
                while right.left is not None:
                    right = right.left

                successor_val = right.val
                root.val = successor_val

                root.right = self.deleteNode(root.right, successor_val)

        return root
