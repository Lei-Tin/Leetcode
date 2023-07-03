class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and len(set(s)) < len(goal):
            return True

        n = len(s)
        diff = []
        for i in range(n):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))

            if len(diff) >= 3:
                return False

        return len(diff) == 2 and diff[0] == diff[1][::-1]

