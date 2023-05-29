class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        lst = [(char, freq) for char, freq in count.items()]
        lst.sort(key=lambda x: x[1], reverse=True)

        ans = ''
        for char, freq in lst:
            ans += char * freq

        return ans

        # Solution 2
        # count = {}
        #
        # for char in s:
        #     count[char] = count.get(char, 0) + 1
        #
        # buckets = [[] for _ in range(len(s) + 1)]
        #
        # for c, freq in count.items():
        #     buckets[freq].append(c)
        #
        # ans = ''
        #
        # for i in range(len(buckets) - 1, 0, -1):
        #     for char in buckets[i]:
        #         ans += char * i
        #
        # return ans
