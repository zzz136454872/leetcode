# 不知道是哪个
class Solution1:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(a):
            out = 0

            for i in range(1, n + 1):
                out += min(a // i, m)

                if a < i:
                    break

            return out

        l = 1
        r = m * n

        while l <= r:
            mid = (l + r) // 2
            tmp = count(mid)

            if tmp < k:
                l = mid + 1
            else:
                r = mid - 1
            print(l, r)

        return l


# sl=Solution()
# m = 2
# n = 3
# k = 6
# print(sl.findKthNumber(m,n,k))


# 字典序的第K小数字
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(prefix, n):
            cur = prefix
            nxt = prefix + 1
            cnt = 0

            while cur <= n:
                cnt += min(n + 1, nxt) - cur
                cur *= 10
                nxt *= 10

            return cnt

        out = 1
        cnt = 1

        while cnt < k:
            tmp = count(out, n)

            if cnt + tmp > k:
                out *= 10
                cnt += 1
            else:
                out += 1
                cnt += tmp

        return out


n = 13
k = 2
print(Solution().findKthNumber(n, k))
