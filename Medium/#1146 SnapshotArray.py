class SnapshotArray:

    def __init__(self, length: int):
        self.s = {i: [[-1, 0]] for i in range(length)}
        self.snaps = 0

    def set(self, index: int, val: int) -> None:
        self.s[index].append([self.snaps, val])

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.s[index]

        l, r = 0, len(snaps) - 1
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            # Go to the latest snapshot even if its the same number
            if snaps[mid][0] <= snap_id:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return snaps[ans][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
