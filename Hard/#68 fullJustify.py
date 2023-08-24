class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)

        i = 0

        while i < n:
            line = []
            curr = 0

            while i < n and curr + len(line) - 1 <= maxWidth:
                curr += len(words[i])
                line.append(words[i])
                i += 1

            if curr + len(line) - 1 > maxWidth:
                i -= 1

                # Remove the last one
                line.pop()
                curr -= len(words[i])

            rem_space = maxWidth - curr
            if len(line) > 1:
                rem_space_each = rem_space // (len(line) - 1)
            else:
                rem_space_each = inf

            l = ''

            if i == n or len(line) == 1:
                l += ' '.join(line)
                l += ' ' * (maxWidth - len(l))
            else:
                spaces = [''] * len(line)
                s = 0

                while s < rem_space:
                    spaces[s % (len(line) - 1)] += ' '
                    s += 1

                for j in range(len(line)):
                    l += line[j] + spaces[j]

            ans.append(l)

        return ans
