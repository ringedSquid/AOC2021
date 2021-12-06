#literal brute force, math is hard
s = 80
fin = open("input.txt", "r")
fin = [int(x) for x in fin.read().split(",")]
for i in range(s):
    for y in range(len(fin)):
        if fin[y] == 0:
            fin[y] = 6
            fin.append(8)
        else:
            fin[y] -= 1

print(len(fin))

