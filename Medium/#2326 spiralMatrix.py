# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]

        curr_x, curr_y = 0, 0
        dx, dy = 0, 1

        curr = head
        while curr != None:
            res[curr_x][curr_y] = curr.val

            curr = curr.next

            if (not (0 <= curr_x + dx < m and 0 <= curr_y + dy < n)) or res[curr_x + dx][
                curr_y + dy] != -1:
                # Rotate
                dx, dy = dy, -dx

            curr_x += dx
            curr_y += dy

        return res
