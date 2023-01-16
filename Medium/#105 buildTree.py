# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder.reverse()
        return self.build(preorder, inorder, 0, len(preorder) - 1)

    def build(self, preorder: List[int], inorder: List[int], left: int, right: int) -> Optional[
        TreeNode]:
        if left > right:
            return None

        else:
            i = inorder.index(preorder.pop())
            tree = TreeNode(inorder[i])

            tree.left = self.build(preorder, inorder, left, i - 1)
            tree.right = self.build(preorder, inorder, i + 1, right)

            return tree
