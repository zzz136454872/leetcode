from typing import List


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.sons = []


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = TreeNode(kingName)
        self.status = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        newNode = TreeNode(childName)
        self.status[childName] = newNode
        self.status[parentName].sons.append(newNode)

    def death(self, name: str) -> None:
        del self.status[name]

    def getInheritanceOrder(self) -> List[str]:
        out = []

        def dfs(root):
            if root is None:
                return

            if root.name in self.status:
                out.append(root.name)

            for son in root.sons:
                dfs(son)

        dfs(self.root)

        return out


class Tester:
    def __init__(self, opList, dataList):
        testedClass = eval(opList[0])
        testedInstance = testedClass(*dataList[0])

        for i in range(1, len(opList)):
            print(opList[i], dataList[i])

            if not dataList[i][0]:
                print(getattr(testedInstance, opList[i])())
            else:
                print(getattr(testedInstance, opList[i])(*dataList[i]))


null = None
opList = [
    "ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth",
    "getInheritanceOrder", "death", "getInheritanceOrder"
]
dataList = [["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"],
            ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null],
            ["bob"], [null]]
Tester(opList, dataList)

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
