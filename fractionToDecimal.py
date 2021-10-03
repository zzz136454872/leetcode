class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = 1

        if numerator < 0:
            numerator = -numerator
            sign = -sign

        if denominator < 0 and numerator:
            denominator = -denominator
            sign = -sign
        nd = numerator // denominator
        numerator = numerator % denominator
        out = ''

        if sign < 0:
            out = '-'
        out += str(nd)

        if numerator == 0:
            return out
        out += '.'
        decimalList = []
        mem = {numerator: 0}
        i = 0

        while numerator != 0:
            numerator *= 10
            numerator, nd = numerator % denominator, numerator // denominator
            decimalList.append(str(nd))

            if numerator in mem:
                out += ''.join(decimalList[:mem[numerator]])
                out += '('
                out += ''.join(decimalList[mem[numerator]:])
                out += ')'

                return out
            i += 1
            mem[numerator] = i

        out += ''.join(decimalList)

        return out


numerator = 11
denominator = 2
numerator = 2
denominator = 1
numerator = 2
denominator = 3
numerator = 4
denominator = 333
numerator = 2
denominator = 3
numerator = 0
denominator = -5
print(Solution().fractionToDecimal(numerator, denominator))
