class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []

        n = len(boxes)

        pref = [0 for _ in range(n)]
        suff = [0 for _ in range(n)]

        left_cnt = 0
        right_cnt = 0

        for i in range(1, n):
            if int(boxes[i - 1]) == 1:
                left_cnt += 1
            if int(boxes[~(i - 1)]) == 1:
                right_cnt += 1

            pref[i] += pref[i - 1] + left_cnt
            suff[~i] += suff[~(i - 1)] + right_cnt

        for i in range(n):
            ans.append(pref[i] + suff[i])

        return ans