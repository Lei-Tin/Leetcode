class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        n, p, z = [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        P, N = set(p), set(n)

        if len(z) > 0:
            for pos in P:
                neg = -1 * pos

                if neg in N:
                    ans.add((neg, 0, pos))

            if len(z) >= 3:
                ans.add((0, 0, 0))

        for pos1 in range(len(p)):
            for pos2 in range(pos1 + 1, len(p)):
                comp = -1 * (p[pos1] + p[pos2])

                if comp in N:
                    ans.add(tuple(sorted((p[pos1], p[pos2], comp))))

        for neg1 in range(len(n)):
            for neg2 in range(neg1 + 1, len(n)):
                comp = -1 * (n[neg1] + n[neg2])

                if comp in P:
                    ans.add(tuple(sorted((n[neg1], n[neg2], comp))))

        return list(ans)
