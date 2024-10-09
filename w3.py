rows = 5
columns = 5
L = []
pattern = ["O", "X"]
# L = ""

ptr_row = 0
ptr_col = 0

while ptr_row < rows:
    ptr_row = ptr_row + 1
    
    ptr_col = 0
    column = []

    while ptr_col < columns:
        ptr_col = ptr_col + 1
        column.append(pattern[(ptr_row + ptr_col) % 2])
    
    L.append(column)

print(L)  # 這行可以自行修改或移除沒關係的
