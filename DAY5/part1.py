def fpnt(array, grid):
    a = array[0]
    b = array[1]
    dir = 1
    if a[0] == b[0]:
        temp = a[1]
        grid[a[0]][temp] += 1
        if a[1] - b[1] > 0:
            dir = -1
        for x in range(abs(a[1]-b[1])):
            temp += dir
            grid[a[0]][temp] += 1

    elif a[1] == b[1]:
        temp = a[0]
        grid[temp][a[1]] += 1
        if a[0] - b[0] > 0:
            dir = -1
        for x in range(abs(a[0]-b[0])):
            temp += dir
            grid[temp][a[1]] += 1

    return grid

def init():
    #processes input from file
    swap = []
    fin = open("input.txt", "r")
    fin = fin.read().split()
    for i in range(len(fin)):
        if fin[i] != '->':
            swap.append([int(x) for x in fin[i].split(",")])
    fin = swap; swap = []
    for i in range(len(fin)//2):
        swap.append([fin[i*2], fin[(i*2)+1]])
    fin = swap; swap = []

    return fin

def main():
    grid = [[0]*1000 for i in range(1000)] #THIS MESSED ME UP BIG TIME OMFG
    vectors = init()
    swap = []
    ov = 0 
    for i in range(len(vectors)):
        grid = fpnt(vectors[i], grid)
    for i in range(len(grid)):
        for y in range(len(grid[i])):
            if grid[i][y] > 1:
                ov += 1
    print(ov)

if __name__ == "__main__":
    main()
