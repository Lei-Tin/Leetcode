class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = []
        curr_sum = 0

        banned = set(banned)

        for i in range(1, n + 1):
            if curr_sum > maxSum:
                break

            if i not in banned:
                if curr_sum + i > maxSum:
                    break
                curr_sum += i
                ans.append(i)

        return len(ans)
