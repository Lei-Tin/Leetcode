class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        image_copy = image.copy()

        # Adding an extra column at the very left side and right side of the image
        for row in image_copy:
            row.insert(0, -1)
            row.append(-1)

        # Adding an extra row in the very end of the image and the start of the image
        image_copy.insert(0, [-1] * len(image[0]))
        image_copy.insert(len(image_copy), [-1] * len(image[0]))

        oldColor = image_copy[sr + 1][sc + 1]

        self.fill(image_copy, sr + 1, sc + 1, newColor, oldColor)

        # Removing the extra borders in image copy
        for row in image_copy:
            row.pop()
            row.pop(0)

        image_copy.pop()
        image_copy.pop(0)

        return image_copy

    def fill(self, image: List[List[int]], sr: int, sc: int, newColor: int, oldColor: int) -> None:
        if image[sr][sc] == newColor or image[sr][sc] != oldColor:
            return

        image[sr][sc] = newColor

        self.fill(image, sr + 1, sc, newColor, oldColor)
        self.fill(image, sr - 1, sc, newColor, oldColor)

        self.fill(image, sr, sc + 1, newColor, oldColor)
        self.fill(image, sr, sc - 1, newColor, oldColor)
