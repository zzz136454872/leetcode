from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        presum = [0]

        for t in tiles:
            presum.append(presum[-1] + t[1] - t[0] + 1)
        r = 0
        res = 0

        for i in range(len(tiles)):

            while r < len(tiles) and tiles[r][0] - tiles[i][0] < carpetLen:
                r += 1

            tmp = presum[r] - presum[i]
            tmp -= max(0, tiles[r - 1][1] - (tiles[i][0] + carpetLen - 1))
            res = max(res, tmp)

        return res


tiles = [[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]]
carpetLen = 10
tiles = [[10, 11], [1, 1]]
carpetLen = 2
print(Solution().maximumWhiteTiles(tiles, carpetLen))
