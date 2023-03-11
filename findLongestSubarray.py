from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        mem = [0]

        for l in array:
            if l.isdigit():
                mem.append(mem[-1] + 1)
            else:
                mem.append(mem[-1] - 1)
        l = 0
        start = 0
        mem2 = {}

        for i in range(len(mem)):
            if mem[i] in mem2:
                if i - mem2[mem[i]] > l:
                    l = i - mem2[mem[i]]
                    start = mem2[mem[i]]
            else:
                mem2[mem[i]] = i

        if l > 0:
            return array[start:start + l]

        return []


array = [
    "A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H",
    "I", "J", "K", "L", "M"
]
array = ["A", "A"]
print(Solution().findLongestSubarray(array))
