class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)

        if k == 1:
            return max(arr[0], arr[1])

        cnt = 0
        curr_winner = arr[0]

        for i in range(1, n):
            if curr_winner > arr[i]:
                cnt += 1
            else:
                curr_winner = arr[i]
                cnt = 1

            if cnt == k:
                return curr_winner

        return curr_winner