class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        pq = []

        visited = set()

        i, j = 0, 0
        heappush(pq, (nums1[i] + nums2[j], i, j))
        visited.add((i, j))

        ans = []

        for _ in range(k):
            if len(pq) == 0:
                break

            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])

            # Visit kind of like dfs
            new_i = i + 1
            new_j = j + 1

            if new_i < n and (new_i, j) not in visited:
                heappush(pq, (nums1[new_i] + nums2[j], new_i, j))
                visited.add((new_i, j))

            if new_j < m and (i, new_j) not in visited:
                heappush(pq, (nums1[i] + nums2[new_j], i, new_j))
                visited.add((i, new_j))

        return ans
