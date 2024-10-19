class Solution:
    def minimumSteps(self, s: str) -> int:
        out_of_place = 0
        ans = 0

        n = len(s)

        for i in range(n):
            # Whenever we see a 0, we have to shift this 0 to the left most
            # This means we have to shift out of place ones to the right

            # At any time in the loop, we must have s[:i] sorted with 0s to 1s
            if s[i] == '0':
                ans += out_of_place
            else:
                out_of_place += 1

        return ans
