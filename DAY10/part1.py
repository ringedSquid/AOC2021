fin = [list(x) for x in open("input.txt", "r").read().split()]
sto = ['(', '[', '{', '<']
dto = {')':'(', ']':'[', '}':'{', '>':'<'}
dti = {')':3, ']':57, '}':1197, '>':25137}
tss = 0
for i in range(len(fin)):
    stk = []
    swap = []
    for y in range(len(fin[i])):
        if fin[i][y] in sto:
            stk.append(fin[i][y])
            fin[i][y] = 'O'
        elif dto[fin[i][y]] == stk[len(stk)-1]:
            stk.pop()
            fin[i][y] = 'C'

    for y in range(len(fin[i])):
        if fin[i][y] != 'O' and fin[i][y] != 'C':
            swap.append(fin[i][y])

    fin[i] = swap

for i in range(len(fin)):
    if fin[i] != []:
        tss += dti[fin[i][0]]

print(tss)

        



