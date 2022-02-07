class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        word_dict = {}

        for word in words:
            if word not in word_dict:
                word_dict[word] = 1

            else:
                word_dict[word] += 1

        i = 0
        length = len(words[0]) * len(words)
        single_length = len(words[0])

        while i + length <= len(s):
            compare_dict = word_dict.copy()

            for j in range(0, len(words) * single_length, single_length):
                if s[i + j:i + j + single_length] in compare_dict:
                    compare_dict[s[i + j:i + j + single_length]] -= 1

            if all(compare_dict[key] == 0 for key in compare_dict):
                ans.append(i)

            i += 1

        return ans
