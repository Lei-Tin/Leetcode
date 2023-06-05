class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time = defaultdict(list)
        times = [releaseTimes[0]]
        for i in range(1, len(releaseTimes)):
            times.append(releaseTimes[i] - releaseTimes[i - 1])

        for i, x in enumerate(keysPressed):
            time[times[i]].append(x)

        return sorted(time[max(time.keys())])[-1]
