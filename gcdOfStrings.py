class Solution:
    def gcdOfStrings(self, str1, str2):
        loc=0
        while loc<len(str1) and loc<len(str2) and str1[loc]==str2[loc]:
            loc+=1
        while not self.verify(str1,str1[:loc]) or not self.verify(str2,str2[:loc]):
            loc-=1
        return str1[:loc]

    def verify(self,string,test):
        if len(test)==0:
            return True
        if len(string)%len(test)!=0:
            return False
        times=len(string)//len(test)
        test=test*times
        return test==string


