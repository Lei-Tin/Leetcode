# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = {}

        def dfs(r: Optional[TreeNode], depth: int):
            if r is None:
                return

            d[depth] = d.get(depth, 0) + r.val
            dfs(r.left, depth + 1)
            dfs(r.right, depth + 1)

        def replace(r: Optional[TreeNode], depth: int):
            if r is None:
                return

            layer_sum = d.get(depth + 1, 0)
            if r.left is not None:
                layer_sum -= r.left.val

            if r.right is not None:
                layer_sum -= r.right.val

            if r.left is not None:
                r.left.val = layer_sum

            if r.right is not None:
                r.right.val = layer_sum

            replace(r.left, depth + 1)
            replace(r.right, depth + 1)

        if root is None:
            return
        root.val = 0
        dfs(root, 0)
        replace(root, 0)

        return root

        # Time limit exceeded solution
        # d = defaultdict(list)

        # def fill(root: Optional[TreeNode], depth: int, par: Optional[TreeNode]):
        #     if root is None:
        #         return

        #     found = False
        #     for i in range(len(d[depth])):
        #         if d[depth][i][0] == par:
        #             d[depth][i][1] += root.val
        #             found = True
        #             break
        #     if not found:
        #         d[depth].append([par, root.val])

        #     fill(root.left, depth + 1, root)
        #     fill(root.right, depth + 1, root)

        # def replace(root: Optional[TreeNode], depth: int, par: Optional[TreeNode]):
        #     if root is None:
        #         return

        #     acc = 0
        #     for i in range(len(d[depth])):
        #         if d[depth][i][0] != par:
        #             acc += d[depth][i][1]

        #     root.val = acc
        #     replace(root.left, depth + 1, root)
        #     replace(root.right, depth + 1, root)

        # fill(root, 0, None)
        # replace(root, 0, None)
        # return root
