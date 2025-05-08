class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars = set(allowed)

        ans = 0
        for word in words:
            flag = True
            for char in word:
                if char not in chars:
                    flag = False
                    break

            ans += int(flag)

        return ans