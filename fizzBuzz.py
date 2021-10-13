from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []

        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    out.append('FizzBuzz')
                else:
                    out.append('Fizz')

                continue

            if i % 5 == 0:
                out.append('Buzz')
            else:
                out.append(str(i))

        return out


n = 15
print(Solution().fizzBuzz(n))
