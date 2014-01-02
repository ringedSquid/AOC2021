cm = 0
fin = open("input.txt", "r")
fin = fin.read().split()
for i in range(len(fin)):
    fin[i] = [int(x) for x in list(fin[i])]
for y in range(len(fin)):
    for x in range(len(fin[y])):
        n = 0
        d = 0
        if x > 0: 
            d += 1
            if fin[y][x] < fin[y][x-1]: n += 1
        if y > 0:
            d += 1
            if fin[y][x] < fin[y-1][x]: n += 1
        if x < len(fin[y])-1:
            d += 1
            if fin[y][x] < fin[y][x+1]: n += 1
        if y < len(fin)-1:
            d += 1
            if fin[y][x] < fin[y+1][x]: n += 1
        
        if n/d == 1:
            cm += fin[y][x] + 1


print(cm)
