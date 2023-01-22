class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # This list contains points in the first index and distances in the second
        points_dist = []

        for point in points:
            points_dist.append((point, point[0] * point[0] + point[1] * point[1]))

        return [point for point, _ in sorted(points_dist, key=lambda x: x[1])[:k]]
