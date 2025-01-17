class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = 'abcdefghijklmnopqrstuvwxyz'

        res_s = ''
        for char in s:
            res_s += str(ord(char) - ord('a') + 1)

        for i in range(k):
            # Find digit sum
            curr_sum = 0

            for char in res_s:
                curr_sum += int(char)

            res_s = str(curr_sum)

        return int(res_s)