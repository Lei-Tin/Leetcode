class Solution:
    def minDeletions(self, s: str) -> int:
        d = Counter(s)

        counts = [d[k] for k in d]
        counts.sort()

        used = set()

        ans = 0
        for i, n in enumerate(counts):
            if n not in used:
                used.add(n)
            else:
                while n in used:
                    ans += 1
                    n -= 1

                if n != 0:
                    used.add(n)

        return ans

