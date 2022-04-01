from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arrp = [num for num in arr if num >= 0]
        arrn = [-num for num in arr if num < 0]

        def check(arr):
            arr.sort()
            # print(arr)

            if len(arr) % 2 != 0:
                return False
            used = [False] * len(arr)
            count = 0
            i = 0
            j = 1

            while count < len(arr) // 2:
                count += 1

                while i < len(arr) and used[i]:
                    i += 1
                used[i] = True

                while j < len(arr) and (used[j] or arr[j] != 2 * arr[i]):
                    j += 1

                if j == len(arr):
                    return False
                used[j] = True
                # print(i,j,used)
                i += 1

            return True

        return check(arrp) and check(arrn)


arr = [3, 1, 3, 6]
arr = [2, 1, 2, 6]
arr = [4, -2, 2, -4]
arr = [1, 2, 4, 16, 8, 4]
arr = [6, -3, 8, -4, 3, 0, 4, -6, 3, 0, 4, -6, 6, -3, 0, 0, -2, 4]
print(Solution().canReorderDoubled(arr))
