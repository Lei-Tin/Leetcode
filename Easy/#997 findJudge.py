class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {i: [] for i in range(1, n + 1)}

        for t1, t2 in trust:
            trusts[t1].append(t2)

        for p in trusts:
            if len(trusts[p]) == 0 and all(p in trusts[i] for i in trusts if i != p):
                return p

        return -1
