row = 3
col = 4  # Just for example

################################

total_number = row * col
ans = []
prime_numbers = []
number_now = 2

# for i in range(total_number):
while len(prime_numbers) <= total_number:
    if number_now == 0:
        prime_numbers.append(2)
    else:
        for j in prime_numbers:
            if number_now % j == 0:
                break
        else:
            prime_numbers.append(number_now)
    
    number_now += 1

for i in range(row):
    ans.append(prime_numbers[i * col: (i + 1) * col])

print(ans)

################################
# [[2, 3, 5, 7],
# [11, 13, 17, 19],
# [23, 29, 31, 37]]
