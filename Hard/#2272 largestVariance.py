class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0

        chars = set(s)
        count = Counter(s)

        for c1 in chars:
            for c2 in chars:
                if c1 == c2:
                    continue

                # Maximum subarray sum
                has_c1, has_c2 = False, False
                subarray_sum = 0

                count_c1, count_c2 = count[c1], count[c2]

                for c in s:
                    if subarray_sum < 0 and count_c1 > 0 and count_c2 > 0:
                        subarray_sum = 0
                        has_c1, has_c2 = False, False
                    if c == c1:
                        subarray_sum += 1
                        count_c1 -= 1
                        has_c1 = True
                    elif c == c2:
                        subarray_sum -= 1
                        count_c2 -= 1
                        has_c2 = True

                    if has_c1 and has_c2:
                        ans = max(ans, subarray_sum)

        return ans
