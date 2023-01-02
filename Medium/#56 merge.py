class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval = sorted(intervals, key=lambda x: x[0])
        merged = [interval[0]]

        for i in interval:
            # Merging algorithm:
            # If the start of the current sorted interval is
            # lesser than the current furthest interval's end
            if i[0] <= merged[-1][-1]:
                merged[-1][-1] = max(merged[-1][-1], i[1])
            else:
                merged.append(i)

        return merged
