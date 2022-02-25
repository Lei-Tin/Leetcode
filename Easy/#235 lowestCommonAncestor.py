# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.findPath(root, p)
        q_path = self.findPath(root, q)

        target = None

        p_path.reverse()
        q_path.reverse()

        for item in p_path:
            if item in q_path:
                target = item
                break

        return self.findNode(root, target)

    def findPath(self, root: 'TreeNode', x: 'TreeNode') -> List[int]:
        path = []

        curr = root

        while curr.val != x.val:
            path.append(curr.val)
            if x.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        path.append(curr.val)

        return path

    def findNode(self, root: 'TreeNode', node_val: int) -> 'TreeNode':
        curr = root

        while curr.val != node_val:
            if node_val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        return curr
