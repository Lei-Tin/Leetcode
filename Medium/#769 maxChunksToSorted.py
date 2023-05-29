class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        curr_max = -inf
        for i in range(len(arr)):
            curr_max = max(curr_max, arr[i])
            if curr_max == i:
                chunks += 1

        return chunks
