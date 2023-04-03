from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        loc = -1

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                loc = i

                break

        if loc == -1:
            return arr

        for j in range(loc, len(arr) - 1):
            if arr[j + 1] >= arr[loc]:
                t = j

                while arr[j] == arr[j - 1]:
                    j -= 1
                arr[loc], arr[j] = arr[j], arr[loc]

                return arr
        arr[loc], arr[-1] = arr[-1], arr[loc]

        return arr


arr = [3, 2, 1]
arr = [1, 1, 5]
arr = [1, 9, 4, 6, 7]
# arr=[3,1,1,3]
print(Solution().prevPermOpt1(arr))
