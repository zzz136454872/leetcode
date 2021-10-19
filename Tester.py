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


if __name__ == '__main__':

    class A:
        def __init__(self, a):
            self.a = a

        def getA(self):
            return self.a

        def getB(self, b):
            return b

    opList = ['A', 'getA', 'getA', 'getB']
    dataList = [[1], None, None, [1234]]
    Tester(opList, dataList)
