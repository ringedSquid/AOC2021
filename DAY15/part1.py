from queue import PriorityQueue

def dij(node, adj, weights, visited):
    costs = {x:float('inf') for x in adj}
    costs[node] = 0
    pq = PriorityQueue()
    pq.put((0, node))
    #sortedmap = sorted(visited.keys(), key=lambda e: distance(e, node)) 
    while not pq.empty():
        (useless, cnode) = pq.get()
        visited[cnode] = True
        for i in adj[cnode]:
            if weights[i] != -1:
                dist = weights[i]
                if visited[i] == False:
                    oldcost = costs[i]
                    newcost = costs[cnode] + dist
                    #print(oldcost, newcost, dist)
                    if newcost < oldcost:
                        pq.put((newcost, i))
                        costs[i] = newcost
    return costs


def init():
    adj = {}
    weights = {}
    visited = {}
    fin = [[int(i) for i in list(x)] for x in open("input.txt", "r").read().split()] 
    end = (len(fin[0])-1, len(fin)-1)
    for i in range(len(fin)):
        for y in range(len(fin[i])):
            if (y, i) not in adj:
                adj[(y, i)] = []
                visited[(y, i)] = False
                weights[(y, i)] = fin[i][y]
                if y > 0: adj[(y, i)].append((y-1, i))
                if y < len(fin[i])-1: adj[(y, i)].append((y+1, i))
                if i > 0: adj[(y, i)].append((y, i-1))
                if i < len(fin)-1: adj[(y, i)].append((y, i+1))

    return adj, weights, visited, end

def main():
    adj, weights, visited, end  = init()
    costs = dij((0,0), adj, weights, visited)
    print(costs[end])
    #print(costs)

main()
