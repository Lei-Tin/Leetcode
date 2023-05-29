# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Optimized solution
        traversed = set()

        while headA is not None:
            traversed.add(headA)
            headA = headA.next

        while headB is not None:
            if headB in traversed:
                return headB

            headB = headB.next

        return None

        # Lesser space complexity solution
        # pointer_a = headA
        # pointer_b = headB
        #
        # while pointer_a is not pointer_b:
        #     pointer_a = headB if pointer_a is None else pointer_a.next
        #     pointer_b = headA if pointer_b is None else pointer_b.next
        #
        # return pointer_a

        # visited = set()
        #
        # curr = headA
        #
        # while curr is not None:
        #     visited.add(curr)
        #
        #     curr = curr.next
        #
        # curr2 = headB
        #
        # size_of_visited = len(visited)
        #
        # while curr2 is not None:
        #     size_of_visited += 1
        #
        #     visited.add(curr2)
        #
        #     if size_of_visited != len(visited):
        #         return curr2
        #
        #     curr2 = curr2.next
        #
        # return None
