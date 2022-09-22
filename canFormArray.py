from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        while True:
            find = False

            for j in range(len(pieces)):
                if pieces[j][0] == arr[0]:
                    cut = arr[:len(pieces[j])]
                    arr = arr[len(pieces[j]):]
                    print(j, pieces, cut)

                    if cut != pieces[j]:
                        return False
                    find = True

                    break

            if not find:
                return False
            del pieces[j]

            if len(pieces) == 0:
                return len(arr) == 0


arr = [15, 88]
pieces = [[88], [15]]
arr = [49, 18, 16]
pieces = [[16, 18, 49]]

arr = [91, 4, 64, 78]
pieces = [[78], [4, 64], [91]]
print(Solution().canFormArray(arr, pieces))
