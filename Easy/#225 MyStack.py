class MyStack:

    def __init__(self):
        self.q = deque()
        self.last = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.last = x

    def pop(self) -> int:
        if len(self.q) == 1:
            ans = self.q.popleft()
            self.q = deque()

            return ans

        q_copy = self.q.copy()
        new_q = deque()
        while len(q_copy) > 1:
            last = q_copy.popleft()
            new_q.append(last)

        self.last = last
        self.q = new_q
        return q_copy.popleft()

    def top(self) -> int:
        return self.last

    def empty(self) -> bool:
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
