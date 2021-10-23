from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # mem=[]
        # for i in range(1,10):
        #     tmp=[str(i)]
        #     for j in range(i+1,10):
        #         tmp.append(str(j))
        #         mem.append(int(''.join(tmp)))
        # mem.sort()
        # print(mem)
        mem = [
            12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789,
            1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678,
            56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789,
            12345678, 23456789, 123456789
        ]
        out = []

        for num in mem:
            if num < low:
                continue

            if num > high:
                break
            out.append(num)

        return out


low = 100
high = 300
low = 1000
high = 13000
print(Solution().sequentialDigits(low, high))
