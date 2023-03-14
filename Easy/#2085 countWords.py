class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = {}

        for word in words1:
            count[word] = count.get(word, 0) + 1

        for word in words2:
            if word in count and count[word] < 2:
                count[word] -= 1

        return sum([1 for word in count if count[word] == 0])
