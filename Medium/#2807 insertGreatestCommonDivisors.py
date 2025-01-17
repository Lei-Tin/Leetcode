# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        @cache
        def gcd(a, b):
            if a == 0:
                return b

            return gcd(b % a, a)

        curr = head
        while curr != None:
            if curr.next is not None:
                next_node = curr.next

                new_node = ListNode(val=gcd(curr.val, next_node.val),
                                    next=next_node)

                curr.next = new_node

                curr = next_node
            else:
                break

        return head