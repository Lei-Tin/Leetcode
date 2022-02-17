class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        unique_chars = set(s + t)

        # for char in s + t:
        #     unique_chars.add(char)

        for char in unique_chars:
            if s.count(char) != t.count(char):
                return False

        return True

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
