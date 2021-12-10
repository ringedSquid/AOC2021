def dfs(vs, g, n, p):
    if n not in vs:
        vs.append(n)
        p.append(n)
        for i in range(len(g[n])):
            dfs(vs, g, g[n][i], p)

cn = []
nd = {}
vs = []
fin = open("input.txt", "r")
fin = fin.read().split()
#preprocessing
for i in range(len(fin)):
    fin[i] = [int(x) for x in list(fin[i])]
    for y in range(len(fin[i])):
        if fin[i][y] == 9:
            fin[i][y] = 'n'
        else:
            fin[i][y] = (i, y)

for y in range(len(fin)):
    for x in range(len(fin[y])):
        if fin[y][x] != 'n':
            a = []
            swap = []
            if x > 0:
                a.append(fin[y][x-1])
            if y > 0:
                a.append(fin[y-1][x])
            if x < len(fin[y])-1:
                a.append(fin[y][x+1])
            if y < len(fin)-1:
                a.append(fin[y+1][x])
            for i in range(len(a)):
                if a[i] != 'n':
                    swap.append(a[i])
            a = swap
            nd[fin[y][x]] = a

for i in range(len(fin)):
    for y in range(len(fin[i])):
        if fin[i][y] != 'n':
            p = []
            dfs(vs, nd, fin[i][y], p)
            if len(p) != 0:
                cn.append(p)

for i in range(len(cn)):
    cn[i] = len(cn[i])

cn = sorted(cn, reverse=True)
print(cn[0]*cn[1]*cn[2])
