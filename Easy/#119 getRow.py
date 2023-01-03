class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 2:
            return [1, 2, 1]

        ans = [1 for _ in range(rowIndex + 1)]

        for i in range(1, (rowIndex + 1) // 2):
            # ans[i] = rowIndex choose i, ans[-i] also = rowIndex choose i
            # To calculate this choose, the formula is rowIndex! / i! (rowIndex - i)!

            # Take example of 4 choose something
            # 4C0 is 1
            # 4C1 is 4! / 3! 1! = 4 / 1
            # 4C2 is 4! / 2! 2! = 4 * 3 / 1 * 2
            # 4C3 is 4! / 1! 3! is the same as 4C1
            # 4C4 is 1

            # As we can see there is a pattern, so for every increase in i, we can just multiply the last value by (rowIndex + 1 - i) / (i)
            ans[i] = ans[-i - 1] = int(ans[i - 1] * (rowIndex + 1 - i) / i)

        if rowIndex > 1 and rowIndex % 2 == 0:
            mid = rowIndex // 2

            ans[mid] = int(ans[mid - 1] * (rowIndex - mid + 1) / mid)

        return ans
