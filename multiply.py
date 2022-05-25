from typing import *


# 不知道是哪个
def add(a, b):
    out = []
    carry = 0

    for i in range(max(len(a), len(b))):
        tmp = carry

        if i < len(a):
            tmp += a[i]

        if i < len(b):
            tmp += b[i]
        carry = tmp // 10
        tmp = tmp % 10
        out.append(tmp)

    if carry == 1:
        out.append(1)

    return out


def smul(a: List, b: int) -> List:
    out = []
    carry = 0

    for i in range(len(a)):
        tmp = a[i] * b + carry
        carry = tmp // 10
        tmp = tmp % 10
        out.append(tmp)

    if carry > 0:
        out.append(carry)

    return out


def toList(a):
    return [int(a[i]) for i in range(len(a) - 1, -1, -1)]


def toStr(a):
    out = ''
    start = False

    for i in range(len(a) - 1, -1, -1):
        if a[i] != 0 or i == 0:
            start = True

        if start:
            out += str(a[i])

    return out


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = toList(num1)
        b = toList(num2)
        out = []

        while len(b) > 0:
            tmp = smul(a, int(b[0]))
            out = add(out, tmp)
            a.insert(0, 0)
            b = b[1:]

        return toStr(out)


# sl=Solution()
# num1='112'
# num2='0'
# print(add([1,1,1],[2,2]))
# print(sl.multiply(num1,num2))


# 递归乘法
class Solution:
    def multiply(self, A: int, B: int) -> int:
        def recursion(k):
            if k == 0:
                return 0

            return A * (k % 2) + 2 * recursion(k >> 1)

        if B < 0:
            return -recursion(-B)

        return recursion(B)


A = 1
B = 10
A = -3
B = -4
print(Solution().multiply(A, B))
