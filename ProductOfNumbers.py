from typing import *

class ProductOfNumbers:

    def __init__(self):
        self.buffer=[1]
        self.now=1
        self.last0=-1

    def add(self, num: int) -> None:
        if num!=0:
            self.now=self.now*num
        else:
            self.last0=len(self.buffer)
        self.buffer.append(self.now)

    def getProduct(self, k: int) -> int:
        if self.last0>=len(self.buffer)-k:
            return 0
        else:
            return self.now//self.buffer[-k-1]

productOfNumbers= ProductOfNumbers();
productOfNumbers.add(3)        # [3]
productOfNumbers.add(0)        # [3,0]
productOfNumbers.add(2)        # [3,0,2]
productOfNumbers.add(5)        # [3,0,2,5]
productOfNumbers.add(4)        # [3,0,2,5,4]
productOfNumbers.getProduct(2) # 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20
productOfNumbers.getProduct(3) # 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40
productOfNumbers.getProduct(4) # 返回  0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8)        # [3,0,2,5,4,8]
print(productOfNumbers.getProduct(2)) # 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32 

