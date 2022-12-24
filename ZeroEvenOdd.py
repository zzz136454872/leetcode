from threading import Semaphore, Thread
from typing import Callable


def pn(x):
    print(x, end=' ')


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zsem = Semaphore(1)
        self.esem = Semaphore(0)
        self.osem = Semaphore(0)

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zsem.acquire()
            printNumber(0)

            if i % 2 == 0:
                self.osem.release()
            else:
                self.esem.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n // 2):
            self.esem.acquire()
            printNumber(2 * i + 2)
            self.zsem.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range((self.n + 1) // 2):
            self.osem.acquire()
            printNumber(2 * i + 1)
            self.zsem.release()


n = 2
n = 5
zeo = ZeroEvenOdd(n)
t1 = Thread(target=zeo.zero, args=(pn, ))
t2 = Thread(target=zeo.even, args=(pn, ))
t3 = Thread(target=zeo.odd, args=(pn, ))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print()
