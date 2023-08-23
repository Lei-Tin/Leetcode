class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = []

        count = Counter(s)

        for k, v in count.items():
            heappush(pq, (-v, k))

        ans = ''
        prev = ''

        i = 0

        while i < len(s):
            char_a = heappop(pq)

            if char_a[1] != prev:
                ans += char_a[1]
                prev = char_a[1]

                if char_a[0] == 0:
                    break

                heappush(pq, (char_a[0] + 1, char_a[1]))
            else:
                if not pq:
                    break

                char_b = heappop(pq)
                if char_b[0] == 0:
                    break

                ans += char_b[1]
                prev = char_b[1]

                heappush(pq, (char_a[0], char_a[1]))
                heappush(pq, (char_b[0] + 1, char_b[1]))

            i += 1

        if i < len(s):
            return ''

        return ans
