class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = [True] + [False for _ in range(n)]

        # Sort so that it can break directly
        # wordDict.sort(key=lambda x: len(x))

        for i in range(n + 1):
            for word in wordDict:
                m = len(word)

                if i - m < 0:
                    # For sorting
                    # break
                    continue


                if s[i - m:i] == word and d[i - m if i - m > 0 else 0]:
                    d[i] = True

        return d[n]

        # q = deque([0])
        # n = len(s)
        # visited = set()
        # visited.add(0)

        # while q:
        #     curr_idx = q.popleft()

        #     for word in wordDict:
        #         m = len(word)

        #         if s[curr_idx:curr_idx + m] == word:
        #             if curr_idx + m == n:
        #                 return True

        #             if curr_idx + m in visited:
        #                 continue
        #             q.append(curr_idx + m)
        #             visited.add(curr_idx + m)


        # return False
