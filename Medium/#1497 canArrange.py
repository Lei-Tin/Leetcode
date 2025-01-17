class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = {i: 0 for i in range(k)}

        for n in arr:
            cnt[n % k] += 1

        n = len(arr)

        print(cnt)

        for i in range(1, k // 2 + 1):
            if cnt[i] != cnt[k - i]:
                return False

        return cnt[0] % 2 == 0