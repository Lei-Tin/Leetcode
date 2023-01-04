class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        interval = sorted(intervals, key=lambda x: x[1])
        merged = 0
        end = -5 * 10 ** 4 - 1

        for i in interval:
            # Merging count algorithm:
            # In the current latest end time in a sorted interval
            # if we meet any interval that has a start time larger than ending, then we want to change the end
            # Otherwise, we have one overlapping interval and we need to add one
            if i[0] >= end:
                end = i[1]
            else:
                merged += 1

        return merged
