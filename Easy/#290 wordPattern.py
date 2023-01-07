class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()

        if len(pattern) != len(lst):
            return False

        patToWord = {}
        wordToPat = {}

        for i in range(len(pattern)):
            if pattern[i] not in patToWord and lst[i] not in wordToPat:
                patToWord[pattern[i]] = lst[i]
                wordToPat[lst[i]] = pattern[i]
            else:
                if patToWord.get(pattern[i], False) != lst[i] or wordToPat.get(lst[i], False) != \
                        pattern[i]:
                    return False

        return True
