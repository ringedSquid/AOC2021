def path(adj, visited, sums, node, dest, grid):
    risk = 0
    ld = [100, 10]
    for i in adj[node]:
        if visited[i] == False:
            if grid[i] < ld[1]:
                ld = [i, grid[i]]
            if grid[i] == grid[ld[0]]:
                if sums[i] < sums[ld[0]]:
                    ld = [i, grid[i]]
            visited[i] = True
    risk += ld[1]
    print(ld)
    risk += path(adj, visited, sums, ld[0], dest, grid)
    return risk






def init():
    adj = {}
    visited = {}
    sums = {}
    grid = {}
    fin = [[int(i) for i in list(x)] for x in open("tnput.txt", "r").read().split()]
    end = (len(fin)-1, len(fin[0])-1)
    for i in range(len(fin)):
        for y in range(len(fin[i])):
            if (y, i) not in adj:
                adj[(y, i)] = []
                visited[(y, i)] = False
                grid[(y, i)] = fin[i][y]
            if y > 0: adj[(y, i)].append((y-1, i))
            if y < len(fin[i])-1: adj[(y, i)].append((y+1, i))
            if i > 0: adj[(y, i)].append((y, i-1))
            if i < len(fin)-1: adj[(y, i)].append((y, i+1))

    for i in adj:
        if i not in sums:
            sums[i] = 0
        for y in adj[i]:
            sums[i] += fin[y[1]][y[0]]

    return adj, visited, sums, end, grid 

def main():
    adj, visited, sums, end, grid = init()
    visited[(0, 0)] = True
    print(path(adj, visited, sums, (0, 0), end, grid)) 


main()
