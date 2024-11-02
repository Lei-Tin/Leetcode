class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split(' ')

        # Check first last
        if lst[0][0] != lst[-1][-1]:
            return False

        for i in range(len(lst) - 1):
            curr_word = lst[i]
            next_word = lst[i + 1]

            if curr_word[-1] != next_word[0]:
                return False

        return True
