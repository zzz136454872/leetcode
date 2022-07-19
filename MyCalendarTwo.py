from sortedcontainers import SortedDict


class MyCalendarTwo:
    def __init__(self):
        self.mem = SortedDict()

    def book(self, start: int, end: int) -> bool:
        # print('book',start,end)
        self.mem[start] = self.mem.get(start, 0) + 1
        self.mem[end] = self.mem.get(end, 0) - 1

        tmp = 0

        for k in self.mem:
            # print(k,self.mem[k])
            tmp += self.mem[k]

            if tmp > 2:
                self.mem[start] -= 1
                self.mem[end] += 1

                return False

        return True


mc = MyCalendarTwo()
print(mc.book(10, 20))
print(mc.book(50, 60))
print(mc.book(10, 40))
print(mc.book(5, 15))
print(mc.book(5, 10))
print(mc.book(25, 55))
