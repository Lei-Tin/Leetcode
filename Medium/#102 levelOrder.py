# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        curr_queue = [root]
        ans = []

        while len(curr_queue) > 0:
            layer = []
            next_queue = []

            for n in curr_queue:

                if n is None:
                    break

                layer.append(n.val)

                if n.left is not None:
                    next_queue.append(n.left)

                if n.right is not None:
                    next_queue.append(n.right)

            curr_queue = next_queue
            ans.append(layer)

        return ans
