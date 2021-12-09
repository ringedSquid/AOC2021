def fnum(array):
    #messy bullshit function. it works though!
    nt = sorted(array[0].split(), key=len)
    ou = array[1].split()
    for i in range(len(nt)):
        nt[i] = ''.join(sorted(nt[i]))
    for i in range(len(ou)):
        ou[i] = ''.join(sorted(ou[i]))
    dv = [[nt[0], 1], [nt[1], 7], [nt[2], 4], [nt[9], 8]]
    sv = {nt[0] : 1, nt[1] : 7, nt[2] : 4, nt[9] : 8}
    smv = {16 : 0, 15 : 2, 8 : 3, 11 : 5, 19 : 6, 12 : 9}
    fr = []
    for i in range(len(dv)):
        for y in range(len(dv[i][0])):
            for z in range(i+1, len(dv)):
                dv[z][0] = dv[z][0].replace(dv[i][0][y], "")
    for i in range(len(nt)):
        sm = 0
        if nt[i] not in sv:
            for y in range(len(dv)):
                if all(x in nt[i] for x in dv[y][0]):
                    sm += dv[y][1]
            sv[nt[i]] = smv[sm]
    for i in range(len(ou)):
        fr.append(sv[ou[i]])
    return fr
    
def init():
    swap = []
    fin = open("input.txt", "r")
    fin = fin.read().split("\n")
    for i in range(len(fin)):
        if fin[i] != '':
            swap.append(fin[i].split("|"))
    fin = swap
    swap = []
    return fin
def main():
    dc = [0]*10
    fs = 0
    print(dc)
    nts = init()
    for i in range(len(nts)):
        n = fnum(nts[i])
        v = int("".join([str(x) for x in n]))
        fs += v
        for y in range(len(n)):
            dc[n[y]] += 1
    print(dc)
    print("part 1: " + str(dc[1]+dc[4]+dc[7]+dc[8]))
    print("part 2: " + str(fs))

    


if __name__ == "__main__":
    main()
