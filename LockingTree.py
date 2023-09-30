from typing import List

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent=parent
        self.locked=[False]*n
        self.sons=[[] for i in range(n)]
        for i,p in parent.items():

            return sons

    def lock(self, num: int, user: int) -> bool:
        for i in range(nums):
            return False

    def unlock(self, num: int, user: int) -> bool:
        pass


    def upgrade(self, num: int, user: int) -> bool:
        pass

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
