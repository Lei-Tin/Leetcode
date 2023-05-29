class ListNode:
    def __init__(self, key: int = None, val: int = None):
        self.next = None
        self.prev = None

        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.c = capacity
        self.d = {}

    def move_to_front(self, node: ListNode) -> None:
        """Moves the node to the front of the list"""
        self.remove_node(node)
        self.add_node(node)

    def remove_node(self, node: ListNode) -> None:
        """Removes the node from the Linked List"""
        node.next.prev, node.prev.next = node.prev, node.next

    def pop_tail(self) -> ListNode:
        """Pops the last node from the tail"""
        n = self.tail.prev
        self.remove_node(n)
        return n

    def add_node(self, node: ListNode) -> None:
        """Adds the node to a place after the head"""
        n = self.head.next
        n.prev = node
        self.head.next = node
        node.next = n
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            self.move_to_front(self.d[key])
            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            n = ListNode(key, value)
            self.add_node(n)
            self.d[key] = n
        else:
            self.move_to_front(self.d[key])
            self.d[key].val = value

        if len(self.d) > self.c:
            popped = self.pop_tail()
            del self.d[popped.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
