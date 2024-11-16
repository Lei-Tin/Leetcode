class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        c1 = Counter(s)
        c2 = Counter(goal)
        if c1 != c2:
            return False

        if s == goal:
            return True

        # Try all possible shifts
        n = len(s)

        for i in range(1, n):
            s1 = s[:i]
            s2 = s[i:]

            if s2 + s1 == goal:
                return True

        return False
