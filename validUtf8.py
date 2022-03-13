from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        last = 0

        def c0(i):
            s = bin(i)[2:] + '0'
            s = (9 - len(s)) * '0' + s

            return s.find('0')

        for d in data:
            if last == 0:
                tmp = c0(d)

                if tmp == 0:
                    last = tmp
                elif tmp == 2 or tmp == 3 or tmp == 4:
                    last = tmp - 1
                else:
                    return False
            else:
                if c0(d) == 1:
                    last -= 1
                else:
                    return False

        return last == 0


data = [197, 130, 1]
data = [235, 140, 4]
data = [255]
print(Solution().validUtf8(data))
