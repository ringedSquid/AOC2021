fin = [list(x) for x in open("input.txt", "r").read().split()]
opn = [] 
sto = ['(', '[', '{', '<']
dto = {')':'(', ']':'[', '}':'{', '>':'<'}
dti = {'(':1, '[':2, '{':3, '<':4}
tss = []
for i in range(len(fin)):
    stk = []
    for y in range(len(fin[i])):
        if fin[i][y] in sto:
            stk.append(fin[i][y])
            fin[i][y] = 0
        elif dto[fin[i][y]] == stk[len(stk)-1]:
            stk.pop()
            fin[i][y] = 0
        else:
            fin[i][y] = 1

    stk.reverse()
    if sum(fin[i]) == 0:
        opn.append(stk)

for i in range(len(opn)):
    n = 0
    for y in range(len(opn[i])):
        n *= 5
        n += dti[opn[i][y]]

    tss.append(n)

tss = sorted(tss)
print(tss[(len(tss)-1)//2])

        





        



