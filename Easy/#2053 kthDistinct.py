class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)

        distinct = []

        for s in arr:
            if cnt[s] == 1:
                distinct.append(s)

        if k > len(distinct):
            return ''


        return distinct[k - 1]
