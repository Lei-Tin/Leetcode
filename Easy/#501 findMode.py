# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Option 2: In order traversal
        self.arr = []
        self.curr_count = 0
        self.max_count = 0
        self.prev_node = None

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            dfs(node.left)

            self.curr_count = self.curr_count + 1 if self.prev_node == node.val else 1

            if self.curr_count == self.max_count:
                self.arr.append(node.val)
            elif self.curr_count > self.max_count:
                self.arr = [node.val]
                self.max_count = self.curr_count

            self.prev_node = node.val

            dfs(node.right)

        dfs(root)

        return self.arr

        # Option 1: Brute force
        # cnt = {}

        # def dfs(node: Optional[TreeNode]) -> None:
        #     if not node:
        #         return

        #     cnt[node.val] = cnt.get(node.val, 0) + 1

        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)

        # arr = []
        # val = max(cnt.values())
        # for k in cnt:
        #     if cnt[k] == val:
        #         arr.append(k)

        # return arr
