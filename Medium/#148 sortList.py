# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # MergeSort algorithm

        # Handle base case, either None or just one element
        if head is None or head.next is None:
            return head

        slow, fast = head, head.next

        # Splitting the linked list into two halves
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next

        # Removing the element to the end of the left list
        slow.next = None

        lsort = self.sortList(left)
        rsort = self.sortList(right)

        return self.merge(lsort, rsort)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]):
        if left is None:
            return right
        elif right is None:
            return left
        else:
            dummy = ListNode(0)
            headPtr = dummy

            while left is not None and right is not None:
                if left.val <= right.val:
                    dummy.next = left
                    left = left.next
                else:
                    dummy.next = right
                    right = right.next

                dummy = dummy.next

            if left is None:
                dummy.next = right
            elif right is None:
                dummy.next = left

            return headPtr.next
