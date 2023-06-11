class Solution:
    def smallestString(self, s: str) -> str:
        # Optimized solution
        if all(char == 'a' for char in s):
            return 'a' * (len(s) - 1) + 'z'

        non_a_ind = 0
        for i, char in enumerate(s):
            if char != 'a':
                non_a_ind = i
                break

        end_ind = len(s)
        for i in range(non_a_ind, len(s)):
            if s[i] == 'a':
                end_ind = i
                break

        return s[:non_a_ind] + ''.join([chr(ord(char) - 1) for char in s[non_a_ind:end_ind]]) + s[end_ind:]

        # My own solution
#         indices = []
#         for i in range(len(s)):
#             if s[i] == 'a':
#                 indices.append(i)

#         if len(indices) > 0:
#             start = ''.join(chr(ord(char) - 1) for char in s[:indices[0]]) + s[indices[0]:]
#             end = s[:indices[-1] + 1] + ''.join(chr(ord(char) - 1) for char in s[indices[-1] + 1:])
#             ans = [start, end]

#             if len(indices) >= 2:
#                 for i in range(len(indices) - 1):
#                     j, k = indices[i], indices[i + 1]

#                     if k - j > 1:
#                         ans.append(s[:j + 1] + ''.join(chr(ord(char) - 1) for char in s[j + 1:k]) + s[k:])
#                         return min(ans)

#             return min(ans)

#         return ''.join([chr(ord(char) - 1) for char in s])
