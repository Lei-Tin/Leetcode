class TrieNode():
    def __init__(self, val):
        self.children = {}
        self.val = val


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        hash_folder = set(folder)
        root = TrieNode('')

        for entry in folder:
            i = 0
            j = 1
            curr = root

            while j < len(entry):
                while j < len(entry) and entry[j] != '/':
                    j += 1

                substr = entry[i:j]

                # Insert in the trie
                if substr not in curr.children:
                    curr.children[substr] = TrieNode(substr)

                curr = curr.children[substr]

                i = j
                j = i + 1

        # DFS Loop through the Trie
        ans = []

        def solve(r, curr):
            if curr + r.val in hash_folder:
                ans.append(curr + r.val)
                return

            for s in r.children:
                solve(r.children[s], curr + r.val)

        solve(root, '')

        return ans
