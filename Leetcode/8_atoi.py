class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        sign = '+'
        while i < len(s) and s[i] == ' ':
            # Ignore white spaces
            i += 1
        if i < len(s) and s[i] == '-':
            sign = '-'
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1 
        while i < len(s) and s[i] == '0':
            i += 1
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
       
        if sign == '-':
            num = -num

        if num > 2 ** 31 - 1:
            num = 2 ** 31 - 1
        elif num < - 2 ** 31:
            num = - 2 ** 31
        return num
