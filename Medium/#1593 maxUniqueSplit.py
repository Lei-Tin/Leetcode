class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        # WA
        # seen = set()
        # n = len(s)

        # l = 0
        # r = 1

        # while r < n:
        #     subset = s[l:r]

        #     if subset not in seen:
        #         seen.add(subset)

        #         l = r
        #         r = l + 1

        #     else:
        #         r += 1

        # if s[l:r] not in seen:
        #     seen.add(s[l:r])

        # return len(seen)

        n = len(s)

        def solve(i, seen):
            if i == n:
                return 0

            ans = 0

            for j in range(i + 1, n + 1):
                substr = s[i:j]

                if substr not in seen:
                    # Backtrack sol
                    seen.add(substr)
                    # Can split on curr
                    ans = max(ans, 1 + solve(j, seen))
                    seen.remove(substr)

            return ans

        return solve(0, set())
