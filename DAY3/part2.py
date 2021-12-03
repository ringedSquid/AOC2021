#kind of messy code :/
bplace = []
fin = open("input.txt", "r")
oxg = fin.read().split()
cod = oxg.copy()
cbit = 0
def maxcom(array, p, m):
    n = 0
    for x in range(len(array)):
        if array[x][p] == "1":
            n += 1
    if m == 1:
        if n > len(array)/2 or n == len(array)/2:
            return 1
        else:
            return 0
    elif m == 0:
        if n < len(array)/2:
            return 1
        else:
            return 0

def rmpl(array, p, v):
    n = []
    for x in range(len(array)):
        if array[x][p] == str(v):
            n.append(array[x])

    return n

while len(oxg) > 1:
    oxg = rmpl(oxg, cbit, maxcom(oxg, cbit, 1))
    cbit += 1
cbit = 0
while len(cod) > 1:
    cod = rmpl(cod, cbit, maxcom(cod, cbit, 0))
    cbit += 1

oxg = int(oxg[0], 2)
cod = int(cod[0], 2)
print(oxg*cod)








