class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = []
        # cnts = []

        # for word in strs:
        #     cnt = {}
        #     for char in word:
        #         cnt[char] = cnt.get(char, 0) + 1

        #     cnts.append(cnt)

        # seen = []

        # for cnt in cnts:
        #     if cnt not in seen:
        #         seen.append(cnt)
        #         indices = [i for i in range(len(cnts)) if cnt == cnts[i]]
        #         ans.append(indices)

        # for ind in ans:
        #     for i in range(len(ind)):
        #         ind[i] = strs[ind[i]]

        # return ans

        # Optimized solution
        collect = {}

        for word in strs:
            arr = [0 for _ in range(26)]
            for char in word:
                # This maps it to 0 to 25, one of them
                # We don't have uppercase letters
                arr[ord(char) - ord('a')] += 1

            tup = tuple(arr)

            collect[tup] = collect.get(tup, []) + [word]

        return list(collect.values())
