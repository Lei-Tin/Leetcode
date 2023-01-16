# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []

        # Stack 1 is the one where we traverse left to right
        # Stack 2 is the one where we traverse right to left
        s1 = [root]
        s2 = []

        while len(s1) > 0 or len(s2) > 0:
            # We will reassign lst for layer 1 and layer 2, so on and so forth
            lst = []

            while len(s1) > 0:
                node = s1.pop()

                lst.append(node.val)

                # Since s2 needs to go from right to left, we append left first
                if node.left is not None:
                    s2.append(node.left)
                if node.right is not None:
                    s2.append(node.right)

            if len(lst) > 0:
                ans.append(lst.copy())

            lst = []

            while len(s2) > 0:
                node = s2.pop()

                lst.append(node.val)

                # Since s1 needs to go from left to right, we append right first
                if node.right is not None:
                    s1.append(node.right)
                if node.left is not None:
                    s1.append(node.left)

            if len(lst) > 0:
                ans.append(lst.copy())

        return ans
