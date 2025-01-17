class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        w1_cnts = [Counter(w) for w in words1]
        w2_cnts = [Counter(w) for w in words2]

        w2_max_cnts = {}
        for d in w2_cnts:
            for k, v in d.items():
                if k not in w2_max_cnts:
                    w2_max_cnts[k] = v

                w2_max_cnts[k] = max(v, w2_max_cnts[k])

        for i, word1 in enumerate(words1):
            word1_cnt = w1_cnts[i]
            flag = True

            for k, v in w2_max_cnts.items():
                if k not in word1_cnt:
                    flag = False
                    break

                if v > word1_cnt[k]:
                    flag = False
                    break

                if not flag:
                    break

            if flag:
                ans.append(word1)

        return ans