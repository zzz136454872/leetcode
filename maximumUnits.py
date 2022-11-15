from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        res = 0
        i = 0

        while truckSize > 0 and i < len(boxTypes):
            if truckSize > boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                res += boxTypes[i][0] * boxTypes[i][1]
                i += 1
            else:
                res += truckSize * boxTypes[i][1]
                i += 1
                truckSize = 0

        return res


boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
print(Solution().maximumUnits(boxTypes, truckSize))
