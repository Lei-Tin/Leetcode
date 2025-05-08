# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1

        # Step a - 1 times
        for i in range(1, a):
            curr = curr.next

        orig_next = curr.next

        curr.next = list2

        # Prepare to point end of list2 to last
        curr2 = list2
        while curr2.next != None:
            curr2 = curr2.next

        # Step b - a times
        for i in range(b - a + 1):
            orig_next = orig_next.next

        curr2.next = orig_next

        return list1