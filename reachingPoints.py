class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        def reachingSub(a, b):
            if a < sx or b < sy:
                return False

            if a == sx and (b - sy) % sx == 0:
                return True

            if b == sy and (a - sx) % sy == 0:
                return True

            if a > b:
                return reachingSub(a % b, b)

            return reachingSub(a, b % a)

        return reachingSub(tx, ty)


sx = 1
sy = 1
tx = 3
ty = 5
# sx = 1
# sy = 1
# tx = 2
# ty = 2
# sx = 1
# sy = 1
# tx = 1
# ty = 1
print(Solution().reachingPoints(sx, sy, tx, ty))
