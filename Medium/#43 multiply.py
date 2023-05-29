class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Return result
        res = [0 for _ in range(len(num1) + len(num2))]

        a = list(num1)[::-1]
        b = list(num2)[::-1]
        carry = res[:]

        for i in range(len(a)):
            for j in range(len(b)):
                val = int(a[i]) * int(b[j]) + carry[i + j] + res[i + j]

                carry[i + j] = 0

                carry[i + j + 1] += val // 10

                res[i + j] = val % 10

        res[len(a) + len(b) - 1] = carry[len(a) + len(b) - 1]

        ans = ''.join(str(c) for c in res[::-1])

        index = 0
        while ans[index] == '0' and index < len(ans) - 1:
            index += 1

        return ans[index:]
