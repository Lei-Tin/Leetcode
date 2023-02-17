# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # def __init__(self):
    #     self.pre = -100000 - 1
    #     self.ans = 100000 + 1

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Solution 2
        # if root is None:
        #     return 0

        # self.minDiffInBST(root.left)

        # self.ans = min(self.ans, root.val - self.pre)
        # self.pre = root.val

        # self.minDiffInBST(root.right)

        # return self.ans

        # Solution 1
        lst = self.inOrderTraversal(root)

        min_dist = 100000 + 1
        for i in range(len(lst) - 1):
            min_dist = min(min_dist, lst[i + 1] - lst[i])

        return min_dist

    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        if root.left is not None:
            ans.extend(self.inOrderTraversal(root.left))

        ans.append(root.val)

        if root.right is not None:
            ans.extend(self.inOrderTraversal(root.right))

        return ans
