gam = []
eps = []
bplace = []
fin = open("input.txt", "r")
fin = fin.read().split()
for x in range(len(fin)):
    for y in range(len(fin[x])):
        if len(bplace) < y+1:
            bplace.append(0)
        if fin[x][y] == "1":
            bplace[y] += 1

for x in range(len(bplace)):
    if bplace[x] > len(fin)/2:
        gam.append(1)
        eps.append(0)
    else:
        gam.append(0)
        eps.append(1)

gam = int("".join([str(x) for x in gam]), 2)
eps = int("".join([str(x) for x in eps]), 2)

print(gam*eps)





