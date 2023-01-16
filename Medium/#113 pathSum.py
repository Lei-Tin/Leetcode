# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        ans = []
        self.findSum(root, [root.val], targetSum, ans)

        return ans

    def findSum(self, root: Optional[TreeNode], path: List[int], targetSum: int,
                ans: List[List[int]]) -> None:
        if sum(path) == targetSum and not root.left and not root.right:
            ans.append(path)

        else:

            if root.left:
                self.findSum(root.left, path + [root.left.val], targetSum, ans)
            if root.right:
                self.findSum(root.right, path + [root.right.val], targetSum, ans)
