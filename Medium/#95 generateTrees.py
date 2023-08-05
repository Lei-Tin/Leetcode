# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        res = []

        def generate(i: int, l: List[int], r: List[int]) -> List[Optional[TreeNode]]:
            ans = []

            if l == [] and r == []:
                return [TreeNode(i)]

            left = [] if l else [None]
            right = [] if r else [None]

            for j in range(len(l)):
                left.extend(generate(l[j], l[:j], l[j + 1:]))

            for j in range(len(r)):
                right.extend(generate(r[j], r[:j], r[j + 1:]))

            for left_tree in left:
                for right_tree in right:
                    t = TreeNode(i)
                    t.left = left_tree
                    t.right = right_tree
                    ans.append(t)

            return ans

        for i in range(1, n + 1):
            res.extend(generate(i, list(range(1, i)), list(range(i + 1, n + 1))))

        return res

