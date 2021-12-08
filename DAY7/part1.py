fin = open("input.txt", "r")
fin = sorted([int(x) for x in fin.read().split(",")])
me = fin[int(round(len(fin)/2, 0))]
hm = 0
for i in range(len(fin)):
    hm += abs(fin[i]-me)
print(hm)
