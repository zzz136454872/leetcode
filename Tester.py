
class Tester:
    def __init__(self,opList,dataList):
        testedClass=eval(opList[0])
        testedInstance=testedClass(dataList[0])
        for i in range(1,len(opList)):
            if not dataList[i]:
                print(getattr(testedInstance,opList[i])())
            else:
                print(getattr(testedInstance,opList[i])(dataList[i]))

if __name__=='__main__':
    class A:
        def __init__(self,a):
            self.a=a

        def getA(self):
            return self.a

    opList=['A','getA','getA','getA']
    dataList=[1,None,None,None]
    Tester(opList,dataList)

        
