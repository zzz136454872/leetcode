from heapq import heappop, heappush
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_heap = []  #smallest out
        buy_heap = []  #biggest out
        mod = 10**9 + 7

        for order in orders:
            # print(order)
            # print(buy_heap)
            # print(sell_heap)

            if order[2] == 0:  # buy
                while len(sell_heap) > 0 and sell_heap[0][0] <= order[0]:
                    sell_order = heappop(sell_heap)

                    if sell_order[1] < order[1]:
                        order[1] -= sell_order[1]
                    else:
                        sell_order[1] -= order[1]
                        order[1] = 0

                        if sell_order[1] > 0:
                            heappush(sell_heap, sell_order)

                        break

                if order[1] > 0:
                    heappush(buy_heap, [-order[0], order[1]])
            else:  # sell
                while len(buy_heap) > 0 and -buy_heap[0][0] >= order[0]:
                    buy_order = heappop(buy_heap)

                    if buy_order[1] < order[1]:
                        order[1] -= buy_order[1]
                    else:
                        buy_order[1] -= order[1]
                        order[1] = 0

                        if buy_order[1] > 0:
                            heappush(buy_heap, buy_order)

                        break

                if order[1] > 0:
                    heappush(sell_heap, [order[0], order[1]])
        out = 0

        for o in buy_heap:
            out += o[1]

        for o in sell_heap:
            out += o[1]

        return out % mod


sl = Solution()
orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
orders = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
print(sl.getNumberOfBacklogOrders(orders))
