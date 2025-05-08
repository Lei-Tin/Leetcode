class Solution:
    @cache
    def countAndSay(self, n: int) -> str:
        # 1
        # 11
        # 2 1
        # 1 2 11
        # 111221
        # 31 22 11

        if n == 1:
            return '1'

        @cache
        def RLE(s):
            runs = []
            curr_run = 0
            last_char = ''
            for char in s:
                if char != last_char:
                    if last_char != '':
                        runs.extend([str(curr_run), last_char])

                    curr_run = 1
                    last_char = char
                else:
                    curr_run += 1

            runs.extend([str(curr_run), last_char])

            return runs

        # Simulation solution
        return ''.join(RLE(self.countAndSay(n - 1)))