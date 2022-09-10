# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        i = 0

        while i <= k and curr is not None:
            if i == k:
                reverse = self.reverseKNodes(head, k)

                head.next = self.reverseKGroup(curr, k)

                return reverse

            i += 1
            curr = curr.next

        if i == k:
            return self.reverseKNodes(head, k)

        return head

    def reverseKNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # We want to reverse the first k-nodes, and return the new starting point
        curr = head
        last = None

        # We want to loop k times, or k nodes
        while k > 0:
            next_node = curr.next

            curr.next = last
            last = curr

            curr = next_node

            k -= 1

        return last

