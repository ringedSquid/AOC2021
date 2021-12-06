s = 256
fs = 0
fin = open("input.txt", "r")
fin = [int(x) for x in fin.read().split(",")]
nc = [0, 0, 0, 0, 0, 0, 0, 0 ,0]
for i in range(len(fin)):
    nc[fin[i]] += 1

print(nc)

for i in range(s):   
    zc = nc[0]
    for y in range(1, len(nc)):
        nc[y-1] = nc[y]

    nc[6] += zc
    nc[8] = zc

for i in range(len(nc)):
    print(nc[i])
    fs += nc[i]

print(fs)



