class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_dict = {}
        window_size = len(s1)

        for char in s1:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        for i in range(len(s2) - window_size + 1):
            dict_copy = char_dict.copy()

            window = s2[i:i + window_size]

            for char in window:
                if char in dict_copy:
                    dict_copy[char] -= 1

            if all(dict_copy[char] == 0 for char in dict_copy):
                return True

        return False
