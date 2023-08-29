class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        min_penalty = inf
        min_hour = n

        pref = [0] * (n + 1)
        suf = [0] * (n + 1)

        curr = 0
        for i in range(n):
            if customers[i] == 'N':
                curr += 1

            pref[i + 1] = curr

        curr = 0
        for i in range(n - 1, -1, -1):
            if customers[i] == 'Y':
                curr += 1

            suf[i] = curr

        min_penalty = inf
        min_hour = n

        for i in range(n, -1, -1):
            # Calculate penalty
            penalty = pref[i] + suf[i]
            if penalty <= min_penalty:
                min_hour = i
                min_penalty = penalty

        return min_hour
