class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # cnt = Counter(s)
        # cnt['a'] = cnt.get('a', 0)
        # cnt['b'] = cnt.get('b', 0)
        # cnt['c'] = cnt.get('c', 0)

        # for char in cnt:
        #     if cnt[char] < k:
        #         return -1

        # n = len(s)

        # def solve(d, l, r):
        #     if l >= n or r < 0:
        #         return 0

        #     if all(d[key] >= k for key in d):
        #         return 0

        #     # Take left or take right
        #     d[s[l]] = d[s[l]] + 1
        #     steps = 1 + solve(d, l + 1, r)
        #     d[s[l]] = d[s[l]] - 1

        #     d[s[r]] = d[s[r]] + 1
        #     steps = min(1 + solve(d, l, r - 1), steps)
        #     d[s[r]] = d[s[r]] - 1

        #     return steps

        # init_d = {'a': 0, 'b': 0, 'c': 0}
        # return solve(init_d, 0, n - 1)

        # Sliding window solution
        cnt = Counter(s)

        cnt['a'] = cnt.get('a', 0)
        cnt['b'] = cnt.get('b', 0)
        cnt['c'] = cnt.get('c', 0)

        if any(cnt[key] < k for key in cnt):
            return -1

        n = len(s)

        # Slide with different sized windows
        l = 0
        r = 0
        curr_cnt = {'a': 0, 'b': 0, 'c': 0}

        ans = float('inf')

        # Expand when possible
        while r < n:
            curr_cnt[s[r]] += 1
            r += 1

            # Shrink window when possible
            # This means we don't have enough to satisfy at least k
            while any(cnt[key] - curr_cnt[key] < k for key in cnt):
                curr_cnt[s[l]] -= 1
                l += 1

            ans = min(ans, n - (r - l))

        return ans
