class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        sorted_items = sorted(items, key=lambda x: (x[0], x[1]))

        n = len(items)

        max_beauty_at_price = []
        curr_beauty = 0

        for price, beauty in sorted_items:
            curr_beauty = max(beauty, curr_beauty)

            max_beauty_at_price.append((price, curr_beauty))

        res = []
        for query in queries:
            # Find right most
            idx = bisect_right(max_beauty_at_price, query, key=lambda x: x[0])

            if idx == 0:
                res.append(0)
            else:
                res.append(max_beauty_at_price[idx - 1][1])

        return res
