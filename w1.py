price = int(input("Enter the price: "))
payment = int(input("Enter the payment: "))

change = payment - price

changes = {
    50: 0,
    10: 0,
    5: 0,
    1: 0
}

for i in changes.keys():
    changes[i] = change // i
    change %= i

print("Changes:")

for i in changes.keys():
    print(f"{i} * {changes[i]}")