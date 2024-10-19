class Solution:
    def maximumSwap(self, num: int) -> int:
        d = {}

        lst = list(str(num))

        for i, char in enumerate(lst):
            num = int(char)

            d[num] = i

        for i, char in enumerate(lst):
            # Check if there is a larger number that exist after this
            num = int(char)

            for j in range(9, num - 1, -1):
                if d.get(j, -1) != -1 and d[j] > i and j > num:
                    # Swap these two entries and return
                    lst[d[j]], lst[i] = lst[i], lst[d[j]]

                    return int(''.join(lst))

        return int(''.join(lst))
