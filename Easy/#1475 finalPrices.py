class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []

        for i, num in enumerate(prices):
            while len(st) > 0 and prices[st[-1]] >= prices[i]:
                prices[st.pop()] -= prices[i]

            st.append(i)

        return prices
