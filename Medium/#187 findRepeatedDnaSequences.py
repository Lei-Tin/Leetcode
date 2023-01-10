class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()

        for i in range(len(s) - 9):
            curr = s[i:i + 10]
            if curr not in seen:
                seen.add(curr)
            else:
                ans.add(curr)

        return list(ans)
