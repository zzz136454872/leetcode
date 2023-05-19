from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        def cal(a):
            b = 1
            r = 0

            for k in a:
                r += k * b
                b *= -2

            return r

        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        for i in range(len(arr2)):
            arr1[i] += arr2[i]

        i = 0

        while i < len(arr1):
            if i < len(arr1) - 1:
                while arr1[i] >= 2 and arr1[i + 1] >= 1:
                    arr1[i] -= 2
                    arr1[i + 1] -= 1

            if arr1[i] <= 1:
                i += 1

                continue

            while len(arr1) < i + 3:
                arr1.append(0)

            if arr1[i] == 4:
                arr1[i] -= 4
            else:
                arr1[i + 1] += 1
                arr1[i] -= 2
            arr1[i + 2] += 1
            i += 1

        while len(arr1) > 1 and arr1[-1] == 0:
            arr1.pop()

        return arr1[::-1]


arr1 = [1, 1, 1, 1, 1]
arr2 = [1, 0, 1]
arr1 = [0]
arr2 = [0]
arr1 = [0]
arr2 = [1]
print(Solution().addNegabinary(arr1, arr2))
