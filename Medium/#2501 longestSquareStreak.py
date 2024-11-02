class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = {}
        nums.sort()

        for n in nums:
            sqrt = math.sqrt(n)

            if int(sqrt) != sqrt:
                seen[n] = 1
            else:
                int_sqrt = int(sqrt)

                if int_sqrt in seen:
                    seen[n] = seen[int_sqrt] + 1
                else:
                    seen[n] = 1

        max_val = max(seen.values())

        return max_val if max_val != 1 else -1
