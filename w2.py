L = [10, 20, 30, 'ABC', '123', '456']

first_part = L[:(len(L)+1)//2]
second_part = L[(len(L)+1)//2:]

result = second_part + first_part
print('result', result)
