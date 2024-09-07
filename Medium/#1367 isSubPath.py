# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None:
                return True

        # Still has linked list nodes but no more leaves to traverse
        if root is None:
            return False

        def solve(curr_head, curr_root):
            if curr_head is None:
                return True

            # Still has linked list nodes but no more leaves to traverse
            if curr_root is None:
                return False

            # For left and right, we have 2 options
            # Consume the current node and proceed
            # Or don't consume and proceed directly
            return (curr_head.val == curr_root.val) and (solve(curr_head.next, curr_root.left) or solve(curr_head.next, curr_root.right))

        return solve(head, root) or self.isSubPath(head, root.left) or self.isSubPath (head, root.right)
