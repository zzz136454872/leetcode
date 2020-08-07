from typing import *

normal=0
in_single=1
in_multi=2
has_sign=3
has_star=4

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        out=[]
        state=normal
        tmp=''
        for line in source:
            if state!=in_multi:
                state=normal
            for i in range(len(line)):
                if state==normal:
                    if line[i]=='/':
                        state=has_sign
                    tmp+=line[i]
                elif state==has_sign:
                    if line[i]=='/':
                        state=normal
                        tmp=tmp[:-1]
                        break
                    elif line[i]=='*':
                        state=in_multi
                        tmp=tmp[:-1]
                    else:
                        state=normal
                        tmp+=line[i]
                elif state==in_multi:
                    if line[i]=='*':
                        state=has_star
                elif state==has_star:
                    print('has_star',line,i,line[i])
                    if line[i]=='/':
                        state=normal
                    elif line[i]!='*':
                        state=in_multi
            if len(tmp)>0 and state!=in_multi:
                out.append(tmp)
                tmp=''
        return out

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source=["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]

["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
['int main()','{ ',' ', 'int a, b, c;','a = b + c;','}']
sl=Solution()
print(sl.removeComments(source))

                    
                
