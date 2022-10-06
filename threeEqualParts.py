from typing import List


# totally garbage
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = arr.count(1)

        if n % 3 != 0:
            return [-1, -1]

        if n == 0:
            return [0, 2]
        count = 0
        n //= 3

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 1:
                count += 1

                if count == n:
                    loc = i

                    break

        print('flag 1', loc)

        for i in range(len(arr)):
            if arr[i] == 1:
                start = i

                break

        for i in range(len(arr) - loc):
            if arr[i + start] != arr[i + loc]:
                return [-1, -1]
        start += len(arr) - loc

        for i in range(start, loc):
            if arr[i] == 1:
                start2 = i

                break

        for i in range(len(arr) - loc):
            if arr[i + start2] != arr[i + loc]:
                return [-1, -1]

        return [start - 1, start2 + len(arr) - loc]


arr = [1, 0, 1, 0, 1]
arr = [1, 1, 0, 1, 1]
arr = [1, 1, 0, 0, 1]
print(Solution().threeEqualParts(arr))
