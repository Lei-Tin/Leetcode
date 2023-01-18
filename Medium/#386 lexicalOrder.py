class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]

        while len(ans) < n:
            val = ans[-1] * 10
            while val > n:
                val //= 10
                val += 1

                while val % 10 == 0:
                    val //= 10

            ans.append(val)

        return ans
