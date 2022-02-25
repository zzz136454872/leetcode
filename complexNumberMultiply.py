class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def s2n(s):
            s = s.split('+')
            s[0] = int(s[0])
            s[1] = int(s[1][:-1])

            return s

        num1 = s2n(num1)
        num2 = s2n(num2)

        return str(num1[0] * num2[0] - num1[1] * num2[1]) +\
            '+' +\
            str(num1[0] * num2[1] + num1[1] * num2[0]) + 'i'


num1 = "1+1i"
num2 = "1+1i"
num1 = "1+-1i"
num2 = "1+-1i"
print(Solution().complexNumberMultiply(num1, num2))
