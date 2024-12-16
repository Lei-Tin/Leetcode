class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Start, end, val

        sort_end_time = sorted(events, key=lambda x: x[1])
        sort_start_time = sorted(events, key=lambda x: x[0])

        n = len(events)

        max_val_until_end = 0
        end_idx = 0

        ans = 0

        for i in range(n):
            # Ending time lesser than current considered starting time
            while end_idx < n and sort_end_time[end_idx][1] < sort_start_time[i][0]:
                max_val_until_end = max(max_val_until_end, sort_end_time[end_idx][2])  # Best other option we have until this end time that doesn't conflict
                end_idx += 1

            # Consider this start and the highest score possible until this end
            ans = max(ans, sort_start_time[i][2] + max_val_until_end)

        return ans
