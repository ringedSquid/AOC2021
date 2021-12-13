def dfs(pd, visited, cnode, dob):
    if cnode == 'end':
        if dob != 'NULL':
            if visited[dob] == 2:
                return 1
            return 0
        return 1
    tp = 0
    for i in pd[cnode]:
        if i.islower():
            if (i == dob and visited[i] < 2) or (visited[i] == 0):
                visited[i] += 1
                tp += dfs(pd, visited, i, dob)
                visited[i] -= 1
        else:
            visited[i] += 1
            tp += dfs(pd, visited, i, dob)
            visited[i] -= 1
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
        visited[fin[i][1]], visited[fin[i][0]] = 0, 0

    visited['start'] = True 
    return pd, visited


def main():
    pd, visited = init()
    result = 0
    for i in pd.keys():
        if i.islower() and i != 'start' and i != 'end':
            result += dfs(pd, visited, 'start', i)
    result += dfs(pd, visited, 'start', 'NULL')
    print(result)

main()
