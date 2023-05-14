# Was not able to solve it in time.
# Time limit exceeded.
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        d = {}
        p = {}
        c = set()

        for i in range(len(nums)):
            d[i] = nums[i]

        self.search([i for i in range(len(nums))], tuple(), -1, 10 ** 9, 0, d, p, c)

        ans = 0
        for entry in c:
            vals = {d[e] for e in entry}
            ans += p[(min(vals), max(vals))]

        return ans

    def search(self, nums: List[int], curr: Tuple[int], val: int, mi: int, ma: int, d: dict,
               p: dict, c: set) -> None:
        if tuple(sorted(curr)) in c:
            return

        ans = p.get((mi, ma), 0)
        if val != -1:
            if d[val] < mi:
                mi = d[val]
            if d[val] > ma:
                ma = d[val]

            if (mi, ma) not in p:
                p[(mi, ma)] = ma ** 2 * mi

        if len(curr) > 0:
            c.add(tuple(sorted(curr)))

        for i in range(len(nums)):
            self.search(nums[:i] + nums[i + 1:], curr + (nums[i],), nums[i], mi, ma, d, p, c)
