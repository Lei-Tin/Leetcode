class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = set()

        people = {i for i in range(1, n + 1)}
        curr = 0
        i = 1
        while True:
            if curr in seen:
                break

            seen.add(curr)
            curr = (curr + i * k) % n
            i += 1

        return sorted(list(people - {num + 1 for num in seen}))
