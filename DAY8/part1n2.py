def fnum(array):
    nt = sorted(array[0].split(), key=len)
    ou = array[1].split()
    dv = [[nt[0], 1], [nt[1], 7], [nt[2], 4], [nt[9], 8]]
    for i in range(len(dv)):
        for y in range(len(dv[i][0])):
            for z in range(i+1, len(dv)):
                dv[z][0] = dv[z][0].replace(dv[i][0][y], "")

    print(nt, dv)
def init():
    swap = []
    fin = open("tnput.txt", "r")
    fin = fin.read().split("\n")
    for i in range(len(fin)):
        if fin[i] != '':
            swap.append(fin[i].split("|"))
    fin = swap
    swap = []
    return fin
def main():
    nts = init()
    fnum(nts[0])


if __name__ == "__main__":
    main()
