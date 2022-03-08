from typing import List


class Solution:
    def platesBetweenCandles(self, s: str,
                             queries: List[List[int]]) -> List[int]:
        can = []
        cnt = 0
        pre_plates = []

        for i in range(len(s)):
            if s[i] == '|':
                can.append(i)
                pre_plates.append(cnt)
            else:
                cnt += 1
        pre_plates.append(cnt)

        def b_left(loc):
            l = 0
            r = len(can) - 1

            while l <= r:
                mid = (l + r) // 2

                if can[mid] >= loc:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        def b_right(loc):
            l = 0
            r = len(can) - 1

            while l <= r:
                mid = (l + r) // 2

                if can[mid] > loc:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        out = []

        for q in queries:
            l1 = b_left(q[0])
            l2 = b_right(q[1])

            if l2 == 0:
                l2 += 1
            out.append(max(pre_plates[l2 - 1] - pre_plates[l1], 0))

        return out


s = "**|**|***|"
queries = [[2, 5], [5, 9]]
s = "***|**|*****|**||**|*"
queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
s = "*|*|||"
queries = [[0, 0], [1, 3]]
print(Solution().platesBetweenCandles(s, queries))
