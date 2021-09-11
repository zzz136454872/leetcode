from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        out = 0
        mod = 10**9 + 7
        n = len(arr)
        # for i in range(n):
        #     tmp=arr[i]
        #     for j in range(i,n):
        #         tmp=min(tmp,arr[j])
        #          out=(out+tmp)%mod
        leftStack = [0]
        leftMem = [1]
        rightStack = [n - 1]
        rightMem = [1]

        for i in range(1, n):
            while len(leftStack) > 0 and arr[leftStack[-1]] > arr[i]:
                leftStack.pop()

            if len(leftStack) > 0:
                leftMem.append(i - leftStack[-1])
            else:
                leftMem.append(i + 1)
            leftStack.append(i)

        for i in range(n - 2, -1, -1):
            while len(rightStack) > 0 and arr[rightStack[-1]] >= arr[i]:
                rightStack.pop()

            if len(rightStack) > 0:
                rightMem.append(rightStack[-1] - i)
            else:
                rightMem.append(n - i)
            rightStack.append(i)

        # print(len(leftMem))
        # print(len(rightMem))
        rightMem = rightMem[::-1]

        for i in range(n):
            # print(i, leftMem[i], rightMem[i], arr[i])
            out = (out + (leftMem[i] * rightMem[i]) * arr[i]) % mod

        return out


# arr = [3,1,2,4]
arr = [11, 81, 94, 43, 3]
# arr=[1,2,1]
print(Solution().sumSubarrayMins(arr))
