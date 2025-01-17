class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Sliding window
        n = len(blocks)

        cnt = Counter(blocks[:k])
        ans = cnt.get('W', 0)

        for i in range(k, n):
            ans = min(ans, cnt.get('W', 0))
            if ans == 0:
                return 0

            cnt[blocks[i - k]] -= 1
            cnt[blocks[i]] += 1

        return min(ans, cnt.get('W', 0))