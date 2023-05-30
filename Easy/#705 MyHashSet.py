class MyHashSet:
    def __init__(self):
        self.size = 10 ** 5
        self.d = [None for _ in range(self.size)]

    def hash_func(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        new_k = self.hash_func(key)
        curr = self.d[new_k]

        if curr is not None:
            while curr.next is not None and curr.val != key:
                curr = curr.next

            if curr.val == key:
                return

            curr.next = ListNode(key)
        else:
            self.d[new_k] = ListNode(key)

    def remove(self, key: int) -> None:
        new_k = self.hash_func(key)
        prev, curr = None, self.d[new_k]

        if prev is None and curr is None:
            return

        while curr is not None and curr.val != key:
            prev, curr = curr, curr.next

        if curr is None:
            return

        if prev is None:
            self.d[new_k] = curr.next
        else:
            prev.next = curr.next

    def contains(self, key: int) -> bool:
        new_k = self.hash_func(key)
        curr = self.d[new_k]

        while curr is not None and curr.val != key:
            curr = curr.next

        if curr is None:
            return False
        else:
            return True


class ListNode:
    def __init__(self, val: int):
        self.next = None
        self.val = val

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
