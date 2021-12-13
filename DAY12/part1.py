#I had to get "inspiration" 
def dfs(pd, visited, cnode):
    if cnode == 'end':
        return 1
    tp = 0
    for i in pd[cnode]:
        if i.islower():
            if visited[i] == False:
                visited[i] = True
                tp += dfs(pd, visited, i)
                visited[i] = False
        else:
            visited[i] = True
            tp += dfs(pd, visited, i)
            visited[i] = False
    return tp

def init():
    pd = {}
    visited = {}
    fin = [x.split("-") for x in open("input.txt", "r").read().split()]
    for i in range(len(fin)):
        if fin[i][0] not in pd:
            pd[fin[i][0]] = []
        pd[fin[i][0]].append(fin[i][1])
        if fin[i][1] not in pd:
            pd[fin[i][1]] = []
        pd[fin[i][1]].append(fin[i][0])
        visited[fin[i][1]], visited[fin[i][0]] = False, False

    visited['start'] = True 
    return pd, visited


def main():
    pd, visited = init()
    print(dfs(pd, visited, 'start'))


main()
