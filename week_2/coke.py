due = 50

while due > 0:
    print(f"Amount due: {due}")
    payment = int(input("Insert coin: "))
    if payment in [25, 10, 5]:
        due -= payment

print(f"Change owed: {-due}")
