class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = math.inf

    def push(self, val: int) -> None:
        if val < self.minimum:
            self.minimum = val

        self.stack.append((val, self.minimum))

    def pop(self) -> None:
        if len(self.stack) >= 2:
            self.minimum = self.stack[-2][1]

        self.stack.pop()

        if len(self.stack) == 0:
            self.minimum = math.inf

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
