class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ''

        pq = []

        if a > 0:
            heapq.heappush(pq, (-a, 'a'))

        if b > 0:
            heapq.heappush(pq, (-b, 'b'))

        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        while pq:
            # Get max
            curr, char = heapq.heappop(pq)

            if len(s) >= 2 and s[-1] == s[-2] == char:
                # Need to grab another character
                if not pq:
                    # No other character left
                    return s

                # o/w take another
                other, other_char = heapq.heappop(pq)
                s += other_char
                if other + 1 < 0:
                    heapq.heappush(pq, (other + 1, other_char))

                # Push original back
                heapq.heappush(pq, (curr, char))
            else:
                s += char
                if curr + 1 < 0:
                    heapq.heappush(pq, (curr + 1, char))

        return s
