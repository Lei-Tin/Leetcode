class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = sorted(arr)

        rank_dict = {}
        prev = None
        rank = 0

        for entry in ranks:
            if entry != prev:
                rank += 1
                rank_dict[entry] = rank
                prev = entry

        for i, e in enumerate(arr):
            arr[i] = rank_dict[e]

        return arr


