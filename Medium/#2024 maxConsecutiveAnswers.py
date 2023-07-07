class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0

        i = 0
        j = 0

        n = len(answerKey)

        num_t = 0
        num_f = 0

        # Counting the sliding window, keeping at most k T's
        while j < n:
            if answerKey[j] == 'T':
                num_t += 1

            while num_t > k:
                if answerKey[i] == 'T':
                    num_t -= 1
                i += 1

            j += 1
            ans = max(ans, j - i)

        i = 0
        j = 0

        # Counting the sliding window, keeping at most k F's
        while j < n:
            if answerKey[j] == 'F':
                num_f += 1

            while num_f > k:
                if answerKey[i] == 'F':
                    num_f -= 1
                i += 1

            j += 1
            ans = max(ans, j - i)

        return ans
