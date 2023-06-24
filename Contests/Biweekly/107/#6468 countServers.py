# Wasn't able to finish in time
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        times = [log[1] for log in logs]

        res = [0 for _ in range(len(queries))]

        l, r = 0, 0
        occr = {}

        for q, i in sorted(zip(queries, range(len(queries)))):
            while r < len(logs) and logs[r][1] <= q:
                if logs[r][0] not in occr:
                    occr[logs[r][0]] = 0
                occr[logs[r][0]] += 1
                r += 1

            while l < len(logs) and logs[l][1] < q - x:
                occr[logs[l][0]] -= 1
                if occr[logs[l][0]] == 0:
                    del occr[logs[l][0]]
                l += 1

            res[i] = n - len(occr)

        return res
