class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        location = {s[i]: i for i in range(len(s))}

        prev = -1
        currMax = 0

        res = []

        for i in range(len(s)):
            currMax = max(currMax, location[s[i]])

            # This is when we find an enclosed partition
            if currMax == i:
                res.append(currMax - prev)
                prev = currMax

        return res
