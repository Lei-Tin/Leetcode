class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        return self.checkHorizontal(board, word) or self.checkVertical(board, word)

    def checkHorizontal(self, board: List[List[str]], word: str) -> bool:
        # Checking for the reversed word
        revWord = word[::-1]

        words = [word, revWord]

        for row in board:
            # Splitting the horizontal spaces in the current row by "#"
            for space in ''.join(row).split('#'):
                for w in words:
                    if len(w) == len(space) and all(
                            space[i] == w[i] or space[i] == ' ' for i in range(len(w))):
                        return True

        return False

    def checkVertical(self, board: List[List[str]], word: str) -> bool:
        # Checking for the reversed word
        revWord = word[::-1]

        words = [word, revWord]

        # Using zip to get the rotated board state (The columns)
        for col in zip(*board):
            # Splitting the vertical spaces by "#"
            for space in ''.join(col).split('#'):
                for w in words:
                    if len(w) == len(space) and all(
                            space[i] == w[i] or space[i] == ' ' for i in range(len(w))):
                        return True

        return False
