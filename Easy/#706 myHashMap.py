class ListNode:
    def __init__(self, key: int, val: int, n: ListNode):
        self.key = key
        self.val = val
        if n is not None:
            self.next = n
        else:
            self.next = None


class MyHashMap:

    def __init__(self):
        self.length = 10 ** 3

        self.vals = [None for i in range(self.length + 1)]

    def put(self, key: int, value: int) -> None:
        target = self.vals[key // self.length]
        if target is None:
            self.vals[key // self.length] = ListNode(key, value, None)
        else:
            self.vals[key // self.length] = ListNode(key, value, self.vals[key // self.length])

    def get(self, key: int) -> int:
        curr = self.vals[key // self.length]

        while curr is not None:
            if curr.key == key:
                return curr.val

            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        curr = self.vals[key // self.length]

        while curr is not None:
            if curr.key == key:
                curr.val = -1
                return
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
