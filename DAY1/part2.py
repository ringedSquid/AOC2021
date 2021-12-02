cx = 0
sa = []
fin = open("input.txt", "r")
fin = [int(x) for x in fin.read().split()]
for x in range(len(fin)-2):
    sa.append((fin[x]+fin[x+1]+fin[x+2]))

for x in range(1, len(sa)):
    if sa[x] > sa[x-1]:
        cx += 1

print(cx)


