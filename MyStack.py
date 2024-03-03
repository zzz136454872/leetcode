from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()
        self.n = 0

    def push(self, x: int) -> None:
        self.q.append(x)

        for _ in range(self.n):
            self.q.append(self.q.popleft())
        self.n += 1

    def pop(self) -> int:
        self.n -= 1

        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.n == 0


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


opList = ["MyStack", "push", "push", "top", "pop", "empty"]
dataList = [[], [1], [2], [], [], []]
Tester(opList, dataList)
