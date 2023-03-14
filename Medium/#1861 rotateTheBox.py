class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            end = -1
            for i in range(-1, -len(row) - 1, -1):
                # We iterate from the end of the list, to simulate gravity
                if row[i] == '*':
                    end = i - 1
                elif row[i] == '#':
                    # Swap locations with the stone and the rightmost empty spot
                    row[i], row[end] = row[end], row[i]
                    end -= 1

        # Using Zip to rotate the Array
        return list(list(i) for i in zip(*box[::-1]))
