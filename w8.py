#TODO (以下撰寫程式)

def leftpad(s, n = 0, c = '0'):
    if n == 0:
        return s
    else:
        # padding = (c * ((n - len(s)) // len(c) + 1))[:n - len(s)]
        padding = c*(((n - len(s)) // len(c)) + 1)
        number = len(padding) - (n-len(s))
        return padding[number:] + s

#(以上撰寫程式)

s = '1.234'
print(leftpad(s, 8, 'x')) # xxx1.234
print(leftpad(s, 8)) # 0001.234
print(leftpad(s, 15, 'ABCD')) # CDABCDABCD1.234
print(leftpad(s, 0)) # 1.234
print(leftpad(n = 7, c = '@', s = s)) # @@1.234