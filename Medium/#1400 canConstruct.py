class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        cnt = Counter(s)

        num_odd = 0
        for key, v in cnt.items():
            if v % 2 == 1:
                num_odd += 1

        return num_odd <= k