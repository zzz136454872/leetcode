from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        res5, res10 = 0, 0

        for b in bills:
            if b == 5:
                res5 += 1
            elif b == 10:
                res10 += 1

                if res5 > 0:
                    res5 -= 1
                else:
                    return False
            else:
                if res10 > 0:
                    res10 -= 1

                    if res5 > 0:
                        res5 -= 1
                    else:
                        return False
                elif res5 > 2:
                    res5 -= 3
                else:
                    return False

        return True


bills = [5, 5, 5, 10, 20]
bills = [5, 5, 10, 10, 20]
print(Solution().lemonadeChange(bills))
