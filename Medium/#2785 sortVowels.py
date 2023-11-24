class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        v = []
        c = []

        for char in s:
            if char in vowels:
                v.append(char)
            else:
                c.append(char)

        v.sort(key=lambda x: ord(x))

        ans = ''
        v_count = 0
        c_count = 0

        for i in range(n):
            if s[i] in vowels:
                ans += v[v_count]
                v_count += 1
            else:
                ans += c[c_count]
                c_count += 1

        return ans
