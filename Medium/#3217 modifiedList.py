# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nums = set(nums)

        # Doesn't create extra listnodes
        # Updates in place
        curr = head
        while curr.next is not None:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head if head.val not in nums else head.next

        # Doesn't update inplace, create one extra linked list to connect
        # curr = head
        # while curr is not None:
        #     if curr.val not in nums:
        #         dummy_curr.next = curr
        #         dummy_curr = dummy_curr.next

        #         next_node = curr.next
        #         curr.next = None
        #     else:
        #         next_node = curr.next

        #     curr = next_node

        # return dummy.next
