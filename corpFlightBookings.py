from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]],
                           n: int) -> List[int]:
        mem = [0] * (n + 2)

        for book in bookings:
            mem[book[0]] += book[2]
            mem[book[1] + 1] -= book[2]
        now = 0
        out = [0] * n

        for i in range(1, n + 1):
            now += mem[i]
            out[i - 1] = now

        return out


sl = Solution()
bookings = [[1, 2, 10], [2, 2, 15]]
n = 2
bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
print(sl.corpFlightBookings(bookings, n))
