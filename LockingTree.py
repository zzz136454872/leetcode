from typing import List

#WA

class LockingTree:

    def __init__(self, parent: List[int]):
        self.n=len(parent)
        self.parent=parent
        self.locked=[-1]*self.n
        self.sons=[[] for i in range(self.n)]
        for i,p in enumerate(parent):
            if p==-1:
                continue
            self.sons[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]==-1:
            self.locked[num]=user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num]==user:
            self.locked[num]=-1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        p=num
        while p!=-1:
            if self.locked[num]!=-1:
                return False
            p=self.parent[p]
        if not self.travel(num):
            return False
        self.unlockall(num)
        self.locked[num]=user
        return True

    def travel(self,root):
        if self.locked[root]!=-1:
            return True
        for s in self.sons[root]:
            if self.travel(s):
                return True
        return False

    def unlockall(self,root):
        self.locked[root]=-1
        for s in self.sons[root]:
            self.unlockall(s)

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

opList=["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
dataList=[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
# opList=["LockingTree","upgrade","upgrade","unlock","lock","upgrade"]
# dataList=[[[-1,0,3,1,0]],[4,5],[3,8],[0,7],[2,7],[4,6]]

opList = ["LockingTree","upgrade","upgrade","upgrade","upgrade","lock","upgrade","lock","upgrade","lock","lock","lock"]
dataList=[[[-1,0,8,0,7,4,2,3,3,1]],[8,39],[5,28],[6,33],[9,24],[5,22],[1,3],[5,20],[0,38],[5,14],[6,34],[6,28],[3,23]]
Tester(opList,dataList)

