class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for x, y in edges:
            if x in seen:
                return x
            if y in seen:
                return y
            seen.add(x)
            seen.add(y)
