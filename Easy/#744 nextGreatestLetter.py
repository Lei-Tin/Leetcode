class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Dumb approach
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]

        return letters[0]

        # Can optimize with binary search, since the input list is sorted
