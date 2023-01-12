class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.start = None
        self.size = 0

    def get(self, index: int) -> int:
        if not (0 <= index < self.size):
            return -1

        else:
            curr = self.start
            i = 0
            while curr is not None and i != index:
                i += 1
                curr = curr.next

            return curr.val

    def addAtHead(self, val: int) -> None:
        new_start = ListNode(val, self.start)

        self.start = new_start

        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return

        curr = self.start
        while curr.next is not None:
            curr = curr.next

        curr.next = ListNode(val)

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif 0 < index < self.size:
            prev, curr = None, self.start
            i = 0

            while curr is not None and i != index:
                i += 1
                prev, curr = curr, curr.next

            new_node = ListNode(val, curr)

            prev.next = new_node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.start = self.start.next
            self.size -= 1
        elif 0 < index < self.size:
            prev, curr = None, self.start
            i = 0

            while curr is not None and i != index:
                i += 1
                prev, curr = curr, curr.next

            prev.next = curr.next

            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
