from typing import *


# 不知道是哪个
class Solution1:
    def isValid(self, s: str) -> bool:
        pair = {'}': '{', ']': '[', ')': '('}
        stack = []

        for bracklet in s:
            if bracklet in pair.keys():
                if len(stack) > 0 and stack[-1] == pair[bracklet]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracklet)

        return len(stack) == 0


# 标签验证器
class Solution2:
    def isValid(self, code: str) -> bool:
        stack = []

        def isTag(s):
            return s.isalpha() and s.isupper() and 1 <= len(s) <= 9

        i = 0

        while i < len(code):
            # print(i, stack, code[i:])

            if code[i] == '<':
                if i >= len(code) - 1:
                    return False

                if code[i + 1] == '!':
                    loc = code.find(']]>', i)

                    if loc == -1:
                        return False

                    if code[i:i + 9] != '<![CDATA[':
                        return False
                    i = loc + 3
                else:
                    flag = 1

                    if code[i + 1] == '/':
                        flag = -1
                        i += 1
                    loc = code.find('>', i)

                    if loc == -1:
                        return False
                    tag = code[i + 1:loc]

                    if not isTag(tag):
                        return False

                    if flag == 1:
                        stack.append(tag)
                    else:
                        if len(stack) > 0 and stack[-1] == tag:
                            stack.pop()
                        else:
                            return False
                    i = loc + 1
            else:
                i += 1

            if i != len(code) and len(stack) == 0:
                return False

        return len(stack) == 0


# code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
# code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
# code = "<A>  <B> </A>   </B>"
# code = "<DIV>  div tag is not closed  <DIV>"
# code = "<DIV>  unmatched <  </DIV>"
# code = "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
# code = "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
# code = "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
# code = "<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"
# code = "<A<></A<>"
# print(Solution().isValid(code))


# 1003. 检查替换后的词是否有效
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter == 'c':
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(letter)
            else:
                stack.append(letter)
            # print(letter, ''.join(stack))

        return len(stack) == 0


s = "aabcbc"
s = "abcabcababcc"
s = "abccba"
print(Solution().isValid(s))
