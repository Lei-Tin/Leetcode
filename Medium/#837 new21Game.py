class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Corner case with game ending directly
        if k == 0:
            return 1.0

        if k > n:
            return 0.0

        prob = {}
        prob[0] = 1.0
        window_sum = 1.0

        # Highest score possible is k + maxPts - 1
        # Achieved by (k - 1) + maxPts
        # Because game ends when we have k or more score
        for i in range(1, k + maxPts):
            # Time limit exceeded solution
            # for roll in range(1, maxPts + 1):
            #     # Probability of getting a new one is P(old) * 1 / maxPts
            #     # We can only roll again if i - roll < K
            #     if i - roll < k and i - roll >= 0:
            #         prob[i] += prob[i - roll] * 1 / maxPts

            # Optimization:
            # Add a sliding window keeping the sum of the previous maxPts terms
            prob[i] = window_sum / maxPts

            if i < k:
                window_sum += prob[i]
            # We want to remove the probability from the sliding window for each i after maxPts value
            if i - maxPts >= 0:
                window_sum -= prob[i - maxPts]

            # The sliding window has 1, 2, 3, ..., k - 1, k, ..., k, k - 1, ..., 3, 2, 1 items.
            # It slides across the probabilities without a fixed length

        ans = 0.0
        for i in range(k, n + 1):
            ans += prob.get(i, 0.0)

        return ans
