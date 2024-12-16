class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        ans = [0] * n

        if k == 0:
            return ans

        if k > 0:
            curr = sum(code[1:k + 1])
            ans[0] = curr
            for i in range(1, n):
                curr += -code[i] + code[(i + k) % n]
                ans[i] = curr
            return ans
        else:
            k = abs(k)
            curr = sum(code[n - k:n])
            ans[0] = curr
            for i in range(1, n):
                curr += -code[(i - k - 1) % n] + code[i - 1]
                ans[i] = curr
            return ans
