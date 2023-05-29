class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Solution 1
        #         ransom_chars = {}
        #         magazine_chars = {}

        #         for char in ransomNote:
        #             if char not in ransom_chars:
        #                 ransom_chars[char] = 1
        #             else:
        #                 ransom_chars[char] += 1

        #         for char in magazine:
        #             if char not in magazine_chars:
        #                 magazine_chars[char] = 1
        #             else:
        #                 magazine_chars[char] += 1

        #         for char in ransom_chars:
        #             if char in magazine_chars:
        #                 ransom_chars[char] -= magazine_chars[char]

        #         return all(ransom_chars[char] <= 0 for char in ransom_chars)

        # Solution 2
        unique_chars = set()
        for char in ransomNote:
            unique_chars.add(char)

        for char in unique_chars:
            if ransomNote.count(char) > magazine.count(char):
                return False

        return True
