from typing import List


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a % b)

        def add(a, b):
            upper = a[0] * b[1] + a[1] * b[0]
            lower = a[1] * b[1]
            g = gcd(upper, lower)

            return (upper // g, lower // g)

        sign = 1
        tmp = []
        upper = 0
        lower = 0
        hasUpper = False

        for letter in expression:
            print(letter, hasUpper, sign, upper, lower)

            if letter == '/':
                hasUpper = True

                continue

            if letter.isdigit():
                if hasUpper:
                    lower = lower * 10 + int(letter)
                else:
                    upper = upper * 10 + int(letter)

                continue

            if hasUpper:
                tmp.append((upper * sign, lower))
                sign = 1
                hasUpper = False
                upper = 0
                lower = 0

            if letter == '-':
                sign = -1

        tmp.append((upper * sign, lower))
        print(tmp)

        res = (0, 1)

        for item in tmp:
            res = add(res, item)

        return str(res[0]) + '/' + str(res[1])


expression = "-1/2+1/2"
expression = "-1/2+1/2+1/3"
expression = "1/3-1/2"
print(Solution().fractionAddition(expression))
