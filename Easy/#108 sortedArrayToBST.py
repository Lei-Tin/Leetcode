# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.insert(nums, 0, len(nums) - 1)

    def insert(self, nums: List[int], start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None

        else:
            mid = (start + end) // 2

            tree = TreeNode(nums[mid])
            tree.left = self.insert(nums, start, mid - 1)
            tree.right = self.insert(nums, mid + 1, end)

            return tree
