class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # Sorts the word by decreasing length then alphabetical order
        dictionary.sort(key=lambda s: (-len(s), s))

        for word in dictionary:
            if self.canForm(s, word):
                return word

        return ''

    def canForm(self, s1: str, s2: str) -> bool:
        # Returns if s1 can form s2 by deleting some of the characters

        i = 0

        for char in s1:
            if i < len(s2) and char == s2[i]:
                i += 1

            if i == len(s2):
                return True

        return False
