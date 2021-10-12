class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = 1

        if dividend < 0:
            sign = -sign
            dividend = -dividend

        if divisor < 0:
            sign = -sign
            divisor = -divisor
        i = 0

        while divisor < dividend:
            divisor <<= 1
            i += 1
        out = 0

        while i >= 0:
            if dividend >= divisor:
                dividend -= divisor
                out += 1 << i
            divisor >>= 1
            i -= 1

        return out * sign


dividend = 10
divisor = 3
# dividend = 7
# divisor = -3

# dividend=-2147483648
# divisor=-3
print(Solution().divide(dividend, divisor))
