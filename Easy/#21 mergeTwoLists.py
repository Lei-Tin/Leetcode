# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[
        ListNode]:
        curr1, curr2 = list1, list2

        newList = ListNode()

        # To keep track of our head node
        head = newList

        while curr1 is not None and curr2 is not None:

            if curr1.val < curr2.val:
                newList.next = curr1
                curr1 = curr1.next

            else:
                newList.next = curr2
                curr2 = curr2.next

            newList = newList.next

        if curr1 is None:
            newList.next = curr2

        if curr2 is None:
            newList.next = curr1

        return head.next

#         if list1 is None:
#             return list2

#         if list2 is None:
#             return list1

#         if list1.val > list2.val:
#             list1, list2 = list2, list1

#         list1.next = self.mergeTwoLists(list2, list1.next)

#         return list1


