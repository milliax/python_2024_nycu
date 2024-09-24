L = [10, 20, 30, 'ABC', '123', '456', 'XYZ']

first_part = L[:len(L)//2]
second_part = L[len(L)//2:]

if (len(L) % 2):
    first_part = L[:len(L)//2+1]
    second_part = L[len(L)//2+1:]

result = second_part + first_part
print('result', result)
