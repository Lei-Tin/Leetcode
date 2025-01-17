# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # length = 0

        # curr = node
        # while curr:
        #     length += 1
        #     curr = curr.next

        # for i in range(length - 2):
        #     node.val = node.next.val
        #     node = node.next

        # node.val = node.next.val
        # node.next = None

        node.val = node.next.val
        node.next = node.next.next