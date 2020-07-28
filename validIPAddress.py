from typing import *

class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            if '.' in IP:
                ip=IP.split('.')
                if len(ip)!=4:
                    return 'Neither'
                for num in ip:
                    num1=int(num)
                    if num1==0 and len(num)>1:
                        return 'Neither'
                    if num1>0 and num[0]=='0' or num1>=256:
                        return 'Neither'
                return 'IPv4'
            else:
                ip=IP.split(':')
                if len(ip)!=8:
                    return 'Neither'
                for num in ip:
                    num1=int(num,base=16)
                    if len(num)==0 or len(num)>4:
                        return 'Neither'
                return 'IPv6'
        except Exception:
            return 'Neither'
    
#ip="20EE:FGb8:85a3:0:0:8A2E:0370:7334"
ip="12.0.1.123"
sl=Solution()
print(sl.validIPAddress(ip))
