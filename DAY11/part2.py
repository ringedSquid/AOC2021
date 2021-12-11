def rset(grid, n):
    for i in range(len(grid)):
        for y in range(len(grid)):
            if grid[i][y] > 9:
                grid[i][y] = 0
                n += 1
    return grid, n

def flup(grid, a, c):
    pl = len(a)
    for i in range(len(grid)):
        for y in range(len(grid)):
            if grid[i][y] > 9 and [i, y] not in a:
                a.append([i, y])
                for x in ([i-1,y],[i+1,y],[i,y-1],[i,y+1],[i-1,y-1],[i-1,y+1],[i+1,y-1],[i+1,y+1]):
                    try:
                        if x[0] > -1 and x[1] > -1:
                            grid[x[0]][x[1]] += 1
                    except:
                        pass
    if len(a) == pl:
        c = False

    return grid, a, c
                
def inup(grid):
    for i in range(len(grid)):
        for y in range(len(grid[i])):
            grid[i][y] += 1
    return grid

def init():
    fin = [list(x) for x in open("input.txt", "r").read().split()]
    for i in range(len(fin)):
        fin[i] = [int(x) for x in fin[i]]
    return fin

def main():
    grid = init()
    fc = 0
    counter = 0
    while fc != len(grid)*len(grid[0]):
        fc = 0
        ppd = []
        c = True
        grid = inup(grid)
        while c == True:
            grid, ppd, c = flup(grid, ppd, c)
        grid, fc = rset(grid, fc)
        counter += 1

    print(counter)


main()



