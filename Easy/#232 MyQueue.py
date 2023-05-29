class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        lst = []
        q = self.queue.copy()

        while len(q) != 0:
            lst.append(q.pop())

        val = lst.pop()

        # The queue with the first item removed
        queue_removed = []

        while len(lst) != 0:
            queue_removed.append(lst.pop())

        self.queue = queue_removed

        return val

    def peek(self) -> int:
        lst = []
        q = self.queue.copy()

        while len(q) != 0:
            lst.append(q.pop())

        return lst.pop()

    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
