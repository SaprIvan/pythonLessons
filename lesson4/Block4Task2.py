size = input()
size = int(size)
for i in range(size):
    for k in range(size):
        print("+--", end="")
    print("+")
    if i == size-1: break
    for j in range(size):
        print("|  ", end="")
    print("|\r")