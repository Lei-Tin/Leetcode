from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {char: order.index(char) for char in order}

        words_lst = []

        for word in words:
            word_lst = []

            for i in range(max([len(s) for s in words])):
                try:
                    word_lst.append(order_dict[word[i]])

                except IndexError:
                    word_lst.append(-1)

            words_lst.append(word_lst)

        for i in range(len(words_lst) - 1):
            for j in range(len(words_lst[0])):
                if words_lst[i][j] > words_lst[i + 1][j]:
                    return False

                elif words_lst[i][j] == words_lst[i + 1][j]:
                    continue

                else:
                    break

        return True


if __name__ == '__main__':
    s = Solution()
