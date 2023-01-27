class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_one = -1
        diff_two = -1

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff_one == -1:
                    diff_one = i
                elif diff_two == -1:
                    diff_two = i
                else:
                    return False

        return s1[diff_one] == s2[diff_two] and s1[diff_two] == s2[diff_one]
