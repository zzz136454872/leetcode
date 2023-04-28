from heapq import heappop, heappush


class DinnerPlates:
    def __init__(self, capacity: int):
        self.stacks = []
        self.valid = []
        self.capacity = capacity

    def push(self, val: int) -> None:
        while len(self.valid) > 0:
            a = self.valid[0]

            if a >= len(self.stacks):
                heappop(self.valid)

                continue

            if len(self.stacks[a]) == self.capacity:
                heappop(self.valid)

                continue
            self.stacks[a].append(val)

            if len(self.stacks[a]) == self.capacity:
                heappop(self.valid)

            return

        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)

        # print(self.stacks)

    def pop(self) -> int:
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()

        if len(self.stacks) > 0:
            # print(self.stacks)

            return self.stacks[-1].pop()
        # print(self.stacks)

        return -1

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            # print(self.stacks)

            return -1

        if len(self.stacks[index]) == 0:
            # print(self.stacks)

            return -1
        v = self.stacks[index].pop()

        if index == len(self.stacks) - 1 and len(self.stacks[index]) == 0:
            self.stacks.pop()
        else:
            heappush(self.valid, index)
        # print(self.stacks)

        return v


class Tester:
    def __init__(self, opList, dataList):
        testedClass = eval(opList[0])
        testedInstance = testedClass(*dataList[0])

        for i in range(1, len(opList)):
            print(opList[i], dataList[i])

            if not dataList[i]:
                print(getattr(testedInstance, opList[i])())
            else:
                print(getattr(testedInstance, opList[i])(*dataList[i]))


opList = [
    "DinnerPlates", "push", "push", "push", "push", "push", "popAtStack",
    "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop",
    "pop"
]
dataList = [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [],
            [], [], []]
Tester(opList, dataList)
