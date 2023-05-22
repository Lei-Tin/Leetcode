class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1, O(n)
        count = Counter(nums)
        frequency = defaultdict(list)

        for c in count:
            frequency[count[c]].append(c)

        ans = []
        for i in range(len(nums), -1, -1):
            ans.extend(frequency[i])

        return ans[:k]

        # Solution 2, O(n log n)
        # pq = []

        # count = Counter(nums)

        # for n in count:
        #     heappush(pq, (-count[n], n))

        # ans = []
        # for i in range(k):
        #     ans.append(heappop(pq)[1])

        # return ans

        # Solution 3, O(n)
        # count = {}
        # buckets = [[] for _ in range(len(nums))]
        #
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        #
        # for num in count:
        #     buckets[count[num] - 1].append(num)
        #
        # j = len(nums) - 1
        #
        # ans = []
        # while len(ans) < k:
        #     if len(buckets[j]) > 0:
        #         ans.append(buckets[j].pop())
        #     else:
        #         j -= 1
        #
        # return ans
