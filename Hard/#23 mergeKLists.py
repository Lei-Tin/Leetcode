# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        answer = ListNode()

        start = answer

        # We have a bunch of currs in here
        lst_of_ptrs = [curr for curr in lists]

        while any(curr is not None for curr in lst_of_ptrs):

            while any(curr is None for curr in lst_of_ptrs):
                lst_of_ptrs.pop(lst_of_ptrs.index(None))

            vals = [curr.val for curr in lst_of_ptrs if curr is not None]

            min_val = min(vals)
            min_index = vals.index(min_val)

            lst_of_ptrs[min_index] = lst_of_ptrs[min_index].next

            curr = ListNode(min_val)

            answer.next = curr

            answer = answer.next

        return start.next
