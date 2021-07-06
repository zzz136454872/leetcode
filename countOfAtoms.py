from typing import *


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def count(nf):
            # print(nf)

            if nf.count('(') == 0:
                log = {}
                name = ''

                for i in range(len(nf)):
                    l = nf[i]

                    if l.isupper():
                        if name != '':
                            if name not in log.keys():
                                log[name] = num_count
                            else:
                                log[name] += num_count
                        name = l
                        num_count = 1
                    elif l.islower():
                        name += l
                    elif l.isdigit():
                        if nf[i - 1].isdigit():
                            num_count = num_count * 10 + int(l)
                        else:
                            num_count = int(l)

                if name != '':
                    if name not in log.keys():
                        log[name] = num_count
                    else:
                        log[name] += num_count
                # print(log)

                return log
            i = 0
            log = {}
            level = 0
            name = ''

            while i < len(nf):
                l = nf[i]

                if level == 0:
                    if l.isupper():
                        if name != '':
                            if name not in log.keys():
                                log[name] = num_count
                            else:
                                log[name] += num_count
                        name = l
                        num_count = 1
                    elif l.islower():
                        name += l
                    elif l.isdigit():
                        if nf[i - 1].isdigit():
                            num_count = num_count * 10 + int(l)
                        else:
                            num_count = int(l)
                    elif l == '(':
                        if name != '':
                            if name not in log.keys():
                                log[name] = num_count
                            else:
                                log[name] += num_count
                        name = ''
                        level += 1
                        start = i + 1
                    i += 1
                else:
                    num_count = 1

                    while level > 0:
                        l = nf[i]

                        if l == '(':
                            level += 1
                        elif l == ')':
                            level -= 1

                            if level == 0:
                                nlog = count(nf[start:i])
                        i += 1

                    if i < len(nf) and nf[i].isdigit():
                        num_count = int(nf[i])
                        i += 1

                    while i < len(nf) and nf[i].isdigit():
                        num_count = num_count * 10 + int(nf[i])
                        i += 1

                    for k, v in nlog.items():
                        if k not in log.keys():
                            log[k] = num_count * v
                        else:
                            log[k] += num_count * v

            if name != '':
                if name not in log.keys():
                    log[name] = num_count
                else:
                    log[name] += num_count
            # print(log)

            return log

        c = count(formula)
        c = list(c.items())
        c.sort()
        out = ''

        for item in c:
            out += item[0]

            if item[1] > 1:
                out += str(item[1])

        return out


sl = Solution()
formula = "Mg(OH)2"
print(sl.countOfAtoms(formula))
