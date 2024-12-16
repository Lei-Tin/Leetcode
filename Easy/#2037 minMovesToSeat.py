class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        ans = 0
        n = len(seats)

        for i in range(n):
            ans += abs(seats[i] - students[i])

        return ans
