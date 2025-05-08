class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            g[u].append(v)

        @cache
        def dfs(start: int, end: int) -> bool:
            if start == end:
                return True
            
            for neighbor in g[start]:
                if dfs(neighbor, end):
                    return True

            return False

        ans = []

        for q in queries:
            start, end = q
            ans.append(dfs(start, end))

        return ans