import heapq


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        heap = [1]
        value = 0
        i = 0

        while i < k:
            now = heapq.heappop(heap)

            if value != now:
                i += 1
                value = now
                heapq.heappush(heap, value * 3)
                heapq.heappush(heap, value * 5)
                heapq.heappush(heap, value * 7)

        return value


k = 9
k = 5
print(Solution().getKthMagicNumber(k))
