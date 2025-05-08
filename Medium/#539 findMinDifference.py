class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Step 1: convert to minutes
        mins = []
        for time in timePoints:
            hrs, minutes = time.split(':')
            mins.append(int(minutes) + 60 * int(hrs))

        mins.sort()
        n = len(timePoints)

        ans = float('inf')

        for i in range(n - 1):
            ans = min(ans, mins[i + 1] - mins[i])
        
        # Special check for wrap around
        ans = min(ans, (mins[0] - mins[-1]) % (60 * 24))
        return ans