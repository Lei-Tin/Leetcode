class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Optimized solution
        oddSet = set()

        for char in s:
            if char not in oddSet:
                oddSet.add(char)
            else:
                oddSet.remove(char)

        if len(oddSet) > 0:
            return len(s) - len(oddSet) + 1

        else:
            return len(s)

        # occur = {}
        #
        # for char in s:
        #     occur[char] = occur.get(char, 0) + 1
        #
        # ans = 0
        #
        # for char in occur:
        #     if occur[char] >= 2:
        #         ans += (occur[char] // 2) * 2
        #
        # if any(occur[char] % 2 == 1 for char in occur):
        #     ans += 1
        #
        # return ans
