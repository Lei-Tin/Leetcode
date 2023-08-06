class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def solve(curr_len: int, curr_unique_music: int) -> int:
            if curr_len == goal:
                return curr_unique_music == n

            # Case with using one song from k units back
            ans = (max(0, curr_unique_music - k) * solve(curr_len + 1, curr_unique_music)) % MOD

            # Case with using one new song from all possible songs
            ans += ((n - curr_unique_music) * solve(curr_len + 1, curr_unique_music + 1)) % MOD

            return ans % MOD

        return solve(0, 0)
