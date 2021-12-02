cx = 0
fin = open("input.txt", "r")
fin = [int(x) for x in fin.read().split()]
for x in range(1, len(fin)):
    if fin[x] > fin[x-1]:
        cx += 1

print(cx)

