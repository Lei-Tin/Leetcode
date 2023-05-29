class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.search(visited, 0, rooms)

        return len(visited) == len(rooms)

    def search(self, visited: set, key: int, rooms: List[List[int]]) -> None:
        if key not in visited:
            visited.add(key)
            for k in rooms[key]:
                self.search(visited, k, rooms)
