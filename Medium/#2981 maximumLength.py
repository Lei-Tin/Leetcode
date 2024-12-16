class Solution:
    def maximumLength(self, s: str) -> int:
        # Brute force
        # cnt = {}

        # n = len(s)

        # # i is window size
        # for i in range(n - 2, 0, -1):

        #     # j is for sliding the window
        #     for j in range(n - i + 1):
        #         substr = s[j:j + i]

        #         # Ensure only speical substrings
        #         if not all(substr[k] == substr[0] for k in range(len(substr))):
        #             continue

        #         cnt[substr] = cnt.get(substr, 0) + 1
        #         if cnt[substr] == 3:
        #             return len(substr)

        # return -1

        # Binary search
        n = len(s)

        l = 1
        r = n

        def is_valid(l):
            # Check if ther exists a length of l special string that occurs 3 times
            cnt = {}

            for j in range(n - l + 1):
                substr = s[j:j + l]

                if not all(substr[k] == substr[0] for k in range(len(substr))):
                    continue

                cnt[substr] = cnt.get(substr, 0) + 1
                if cnt[substr] == 3:
                    return True

            return False

        if not is_valid(1):
            return -1

        while l < r:
            mid = (l + r) // 2

            if is_valid(mid):
                # Can increase value
                l = mid + 1
            else:
                # Need to decrease
                r = mid

        return l - 1
