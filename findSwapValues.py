from typing import List


class Solution:
    def findSwapValues(self, array1: List[int],
                       array2: List[int]) -> List[int]:
        s1 = sum(array1)
        s2 = sum(array2)

        if (s1 - s2) % 2 != 0:
            return []
        array1.sort()
        array2.sort()
        diff = (s2 - s1) // 2
        j = 0

        for i in range(len(array1)):
            target = array1[i] + diff

            while j < len(array2) and array2[j] < target:
                j += 1

            if j < len(array2) and array2[j] == target:
                return (array1[i], array2[j])

        return []


array1 = [4, 1, 2, 1, 1, 2]
array2 = [3, 6, 3, 3]
array1 = [4, 1, 2, 1, 1, 2]
array2 = [3, 6, 3, 3]
array1 = [1, 2, 3]
array2 = [4, 5, 6]
print(Solution().findSwapValues(array1, array2))
