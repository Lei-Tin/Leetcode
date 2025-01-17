class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pref = [0 for _ in range(n + 1)]

        for l, r, d in shifts:
            if d == 0:
                d = -1
            pref[l] += d
            pref[r + 1] -= d

        for i in range(1, n + 1):
            pref[i] += pref[i - 1]

        ans = ''

        for i, char in enumerate(s):
            new_chr = chr((ord(char) - ord('a') + pref[i]) % 26 + ord('a'))

            ans += new_chr

        return ans