# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Solution 1
        # Creating a list and sum up to n // 2

        # lst = []
        # curr = head
        # while curr is not None:
        #     lst.append(curr.val)
        #     curr = curr.next

        # max_val = 0
        # for i in range(len(lst) // 2):
        #     max_val = max(max_val, lst[i] + lst[~i])

        # return max_val

        # Solution 2
        # Find mid point
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        while slow is not None:
            next_node = slow.next

            slow.next = prev
            prev = slow

            slow = next_node

        curr = head
        max_val = 0
        while prev is not None:
            max_val = max(max_val, curr.val + prev.val)
            curr = curr.next
            prev = prev.next

        return max_val
