# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #         ans = []
        #         lst = []
        #         lst.append(root)

        #         while lst != []:
        #             root = lst.pop()
        #             ans.append(root.val)

        #             if root.left is not None:
        #                 lst.append(root.left)

        #             if root.right is not None:
        #                 lst.append(root.right)

        #         return ans

        if root is None:
            return []

        else:
            ans = []

            ans.extend([root.val])

            ans.extend(self.preorderTraversal(root.left))

            ans.extend(self.preorderTraversal(root.right))

            return ans



