cn = []
fin = open("tnput.txt", "r")
fin = fin.read().split()
for i in range(len(fin)):
    fin[i] = [int(x) for x in list(fin[i])]
    for y in range(len(fin[i])):
        if fin[i][y] == 9:
            fin[i][y] = 0 
        else:
            fin[i][y] = 1

for i in range(len(fin)):
    for y in range(len(fin[i])):


for i in fin:
    print(i)
