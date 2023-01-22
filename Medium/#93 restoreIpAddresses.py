class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.search(s, '', 0, ans)
        return ans

    def search(self, s: str, path: str, length: int, ans: List[str]) -> None:
        if length > 4:
            return
        # We have used up all of the characters available and it gave us a length of 4
        if length == 4 and s == '':
            ans.append(path[:-1])  # Using -1 because we have to get rid of the final dot

        else:
            for i in range(1, 4):

                # We have to break out of this recursive call as soon as we see a bad situation listed below
                # If we don't have enough remaining indices for this split
                if i > len(s):
                    break

                # If we have 2 digits or more but the number begins with 0
                if i > 1 and s[0] == '0':
                    break

                # If we have 3 digits but the value is larger than 255
                if i > 2 and int(s[:3]) > 255:
                    break

                self.search(s[i:], path + s[:i] + '.', length + 1, ans)

            return
