# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        else:
            ans = []

            ans.extend(self.postorderTraversal(root.left))

            ans.extend(self.postorderTraversal(root.right))

            ans.extend([root.val])

            return ans

