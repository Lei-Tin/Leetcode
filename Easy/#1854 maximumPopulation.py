class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0 for _ in range(101)]  # 1950 to 2050

        for start, end in logs:
            years[start - 1950] += 1
            years[end - 1950] -= 1

        max_val = years[0]

        for i in range(1, len(years)):
            years[i] += years[i - 1]
            max_val = max(max_val, years[i])

        for i in range(len(years)):
            if years[i] == max_val:
                return 1950 + i
