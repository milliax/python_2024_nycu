# m, n = 6, 3 #Just for example
m, n = 8,4 #Just for example

################################

L = [[i*n + j if i % 2 == 0 else i*n + (n - 1 - j) for j in range(n)] for i in range(m)]

################################
print(L) #[[0, 1, 2],[5, 4, 3],[6, 7, 8],[11, 10, 9],[12, 13, 14],[17, 16, 15]]