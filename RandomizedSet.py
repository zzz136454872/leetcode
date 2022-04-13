from random import choice


class RandomizedSet:
    def __init__(self):
        self.table = []
        self.loc = dict()

    def insert(self, val: int) -> bool:
        if val in self.loc:
            return False
        self.loc[val] = len(self.table)
        self.table.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.loc:
            return False
        idx = self.loc[val]
        self.table[idx] = self.table[-1]
        self.loc[self.table[idx]] = idx
        self.table.pop()
        del self.loc[val]

        return True

    def getRandom(self) -> int:
        return choice(self.table)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
