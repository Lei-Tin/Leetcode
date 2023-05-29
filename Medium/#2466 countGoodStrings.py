class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Stores the amount of strings that can be formed with '0' zeroes and '1' ones with a specific length
        d = {0: 1}

        for i in range(1, high + 1):
            d[i] = d.get(i - zero, 0) + d.get(i - one, 0)

        return sum(d[i] for i in range(low, high + 1)) % (10 ** 9 + 7)

    # Time Exceeded Solution 1
    # def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    #     res = set()
    #     k = {'0': zero, '1': one}

    #     self.search(k, '', low, high, res)

    #     return len(res) % (10 ** 9 + 7)

    # def search(self, k: dict, curr: str, low: int, high: int, res: set) -> None:
    #     if len(curr) > high:
    #         return

    #     if len(curr) >= low:
    #         res.add(curr)

    #     for char in k:
    #         self.search(k, curr + k[char] * char, low, high, res)
