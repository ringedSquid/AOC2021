def inet(quant, cuant, chart):
    fuant = cuant.copy()
    for i in cuant:
        f = cuant[i]
        insert = chart[i]
        fuant[i] -= 1*f
        fuant[i[0]+insert] += 1*f
        fuant[insert+i[1]] += 1*f
        quant[insert] += 1*f

    return quant, fuant

def init():
    seti = {}
    sequence = open("sequence.txt", "r").read().strip()
    chart = open("input.txt", "r").read().split("\n")
    for i in range(len(chart)):
        if chart[i] != '':
            n = chart[i].split(' -> ')
            seti[n[0]] = n[1]
    return sequence, seti
        
def main():
    sequence, chart = init()
    quant = {}
    cuant = {}
    #holy shit, so many for loops
    for i in chart:
        quant[chart[i]] = 0
        cuant[i] = 0
    for i in range(len(sequence)):
        quant[sequence[i]] += 1
    for i in range(len(sequence)-1):
        cuant[sequence[i:i+2]] += 1
    for i in range(40):
        quant, cuant = inet(quant, cuant, chart)

    print(max(quant.values()) - min(quant.values()))
        


main()
