class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 3
        if len(s) != len(t):
            return False

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            if freq.get(char, -1) < 1:
                return False

            freq[char] = freq[char] - 1

        return True

        # Solution 1
        # unique_chars = set(s + t)
        #
        # # for char in s + t:
        # #     unique_chars.add(char)
        #
        # for char in unique_chars:
        #     if s.count(char) != t.count(char):
        #         return False
        #
        # return True

        # Solution 2

#         s_chars = {}
#         t_chars = {}

#         for char in s:
#             if char not in s_chars:
#                 s_chars[char] = 1
#             else:
#                 s_chars[char] += 1

#         for char in t:
#             if char not in t_chars:
#                 t_chars[char] = 1
#             else:
#                 t_chars[char] += 1

#         return s_chars == t_chars
