class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ops = []
        vs = []
        os = ('!', '&', '|')

        for letter in expression:
            # print(letter,ops,vs)

            if letter == ')':
                tmp = []

                while vs[-1] != '(':
                    tmp.append(vs.pop())
                vs.pop()
                o = ops.pop()

                if o == '!':
                    if tmp[0] == 'f':
                        vs.append('t')
                    else:
                        vs.append('f')
                elif o == '&':
                    if 'f' in tmp:
                        vs.append('f')
                    else:
                        vs.append('t')
                else:
                    if 't' in tmp:
                        vs.append('t')
                    else:
                        vs.append('f')
            elif letter in os:
                ops.append(letter)
            elif letter == ',':
                continue
            else:
                vs.append(letter)

        if vs[0] == 't':
            return True

        return False


expression = "!(f)"
expression = "|(f,t)"
expression = "&(t,f)"
expression = "|(&(t,f,t),!(t))"
print(Solution().parseBoolExpr(expression))
