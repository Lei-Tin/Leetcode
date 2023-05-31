class UndergroundSystem:

    def __init__(self):
        # Maps an ID to an ongoing trip and it's information
        self.trip = {}
        # We can do this because a checkIn is always followed by a checkOut

        # These are dicts mapping from (start, end) to counts and total time taken
        self.routeCounts = {}
        self.routeTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trip[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, startTime = self.trip[id]
        end, endTime = stationName, t
        self.routeCounts[(start, end)] = self.routeCounts.get((start, end), 0) + 1
        self.routeTime[(start, end)] = self.routeTime.get((start, end), 0) + (endTime - startTime)

        del self.trip[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        start, end = startStation, endStation
        return self.routeTime[(start, end)] / self.routeCounts[(start, end)]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
