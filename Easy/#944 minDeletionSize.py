class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0

        for i in range(len(strs[0])):
            curr_str = ''
            for j in range(len(strs)):
                curr_str += strs[j][i]

            if not is_sorted(curr_str):
                count += 1

        return count


def is_sorted(s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False

    return True

