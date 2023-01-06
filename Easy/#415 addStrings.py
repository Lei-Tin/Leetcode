class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        shortest = min(len(num1), len(num2))
        longest = max(len(num1), len(num2))

        if shortest == len(num1):
            n1 = [n for n in num1[::-1]] + ['0' for _ in range(longest - shortest + 1)]
            n2 = [n for n in num2[::-1]] + ['0']
        else:
            n1 = [n for n in num1[::-1]] + ['0']
            n2 = [n for n in num2[::-1]] + ['0' for _ in range(longest - shortest + 1)]

        # This 0 is a placeholder and will be replaced later
        ans = [0 for _ in range(longest + 1)]
        carry = 0

        for i in range(longest):
            val = int(ans[i]) + int(n1[i]) + int(n2[i])
            ans[i] = str(val % 10)
            carry = val // 10
            ans[i + 1] = str(carry)

        if carry == 0:
            return ''.join(ans[len(ans) - 2::-1])

        return ''.join(ans[::-1])
