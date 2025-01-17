class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.arr) >= self.max_size:
            return  # Cannot add

        self.arr.append(x)

    def pop(self) -> int:
        if self.arr:
            return self.arr.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)