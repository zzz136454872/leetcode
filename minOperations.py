from typing import List


# can not remember what this is
class Solution1:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(i) for i in boxes]
        left = [0 for i in boxes]
        right = [0 for i in boxes]
        tmp = 0

        for i in range(len(boxes)):
            left[i] = tmp
            tmp += boxes[i]
        tmp = 0

        for i in range(len(boxes) - 1, -1, -1):
            right[i] = tmp
            tmp += boxes[i]
        tmp = 0

        for i in range(len(boxes)):
            if boxes[i]:
                tmp += i
        out = [tmp]
        print(left, right)

        for i in range(1, len(boxes)):
            tmp += left[i] - right[i - 1]
            out.append(tmp)

        return out


# boxes = "001011"
# sl = Solution()
# print(sl.minOperations(boxes))


# 得到子序列的最少操作次数
class Solution2:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        mem = {}

        for i in range(len(target)):
            mem[target[i]] = i
        arr1 = []

        for num in arr:
            if num in mem:
                arr1.append(mem[num])

        if len(arr1) == 0:
            return len(target)
        stack = [arr1[0]]
        lcs = 1

        for num in arr1[1:]:
            if num > stack[-1]:
                stack.append(num)
                lcs = max(lcs, len(stack))
            else:
                left = 0
                right = len(stack) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if stack[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                lcs = max(lcs, left + 1)
                stack[left] = num

        return len(target) - lcs


# sl = Solution()
#
# target = [5, 1, 3]
# arr = [9, 4, 2, 3, 4]
#
# target = [6, 4, 8, 1, 3, 2]
# arr = [4, 7, 6, 2, 3, 8, 6, 1]

# print(sl.minOperations(target, arr))


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == '../':
                if depth > 0:
                    depth -= 1
            elif log == './':
                continue
            else:
                depth += 1

        return depth


logs = ["d1/", "d2/", "../", "d21/", "./"]
print(Solution().minOperations(logs))
