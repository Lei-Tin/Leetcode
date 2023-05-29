class UF:
    def __init__(self, size):
        self.p = {i: i for i in range(size)}

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        self.p[xp] = yp
        return True
