class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Using Union find
        unionDict = {}

        for i in range(len(s1)):
            self.union(unionDict, s1[i], s2[i])

        ans = ''

        for char in baseStr:
            ans = ans + self.find(unionDict, char)

        return ans


    def find(self, unionDict: dict, c: str) -> str:
        # Finds the root of c in the union dictionary
        if c not in unionDict:
            unionDict[c] = c

        else:
            # Case 1, if the char we are looking for is the root already
            if c == unionDict[c]:
                return c
            else:
                # Case 2 if the char we are looking for is not the root,
                # then we find the root of the current value
                unionDict[c] = self.find(unionDict, unionDict[c])

        return unionDict[c]

    def union(self, unionDict: dict, c1: str, c2: str) -> None:
        rootC1 = self.find(unionDict, c1)
        rootC2 = self.find(unionDict, c2)

        if rootC1 < rootC2:
            unionDict[rootC2] = rootC1
        else:
            unionDict[rootC1] = rootC2
