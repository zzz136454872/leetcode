class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 1
        self.mem = [None] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.mem[idKey] = value
        res = []

        while self.ptr < len(self.mem) and self.mem[self.ptr] != None:
            res.append(self.mem[self.ptr])
            self.ptr += 1

        return res
