# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [ListNode() for _ in range(k)]
        dummies = [res[i] for i in range(k)]
        n = 0

        curr = head
        while curr is not None:
            n += 1
            curr = curr.next

        curr = head
        rem = n % k

        if n // k == 0:
            for i in range(rem):
                res[i].next = curr
                res[i] = res[i].next

                res[i].next, curr = None, curr.next
        else:
            for i in range(k):
                for j in range(n // k):
                    res[i].next = curr
                    res[i] = res[i].next
                    res[i].next, curr = None, curr.next

                if rem > 0:
                    res[i].next = curr
                    res[i] = res[i].next
                    res[i].next, curr = None, curr.next
                    rem -= 1

        return [dummy.next for dummy in dummies]
