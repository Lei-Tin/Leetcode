# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = head
        dummy = ans

        curr = head

        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                while curr.next is not None and curr.val == curr.next.val:
                    curr = curr.next

                curr = curr.next
                ans.next = curr

            else:
                ans = ans.next
                curr = curr.next

        return dummy.next
