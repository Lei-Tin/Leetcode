class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n + 1)]

        i = 0
        while len(friends) > 1:
            # We will use 0 index here
            i = (i + (k - 1)) % len(friends)

            friends.pop(i)

        return friends[0]
