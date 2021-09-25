class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(a) for a in list(str(num))]

        for i in range(len(num) - 1):
            m = -1
            loc = -1

            for j in range(i + 1, len(num)):
                if m <= num[j]:
                    loc = j
                    m = num[j]

            if num[i] < m:
                num[i], num[loc] = num[loc], num[i]

                break

        return int(''.join([str(a) for a in num]))


num = 2736
# num=9973
num = 98368
print(Solution().maximumSwap(num))
