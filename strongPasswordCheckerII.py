class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        cu = 0
        cl = 0
        cn = 0
        cs = 0

        for i in range(len(password)):
            if i > 0 and password[i] == password[i - 1]:
                return False

            if password[i].isupper():
                cu += 1
            elif password[i].islower():
                cl += 1
            elif password[i].isnumeric():
                cn += 1
            elif password[i] in "!@#$%^&*()-+":
                cs += 1

        return cu > 0 and cl > 0 and cn > 0 and cs > 0


password = "IloveLe3tcode!"
password = "Me+You--IsMyDream"
password = "1aB!"
print(Solution().strongPasswordCheckerII(password))
