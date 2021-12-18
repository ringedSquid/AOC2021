def mov(n, encoded, cpos):
    cpos += n
    return int(encoded[cpos-n:cpos], 2), cpos

def decode(encoded, cpos):
    v, cpos = mov(3, encoded, cpos)
    t, cpos = mov(3, encoded, cpos)
    if t == 4:
        while encoded[cpos] == "1":
            cpos = mov(5, encoded, cpos)[1]
        #last set
        cpos = mov(5, encoded, cpos)[1]
    else:
        i, cpos = mov(1, encoded, cpos)
        if i == 0:
            l, cpos = mov(15, encoded, cpos)
            r = cpos
            while cpos - r < l:
                result = decode(encoded, cpos)
                v += result[0]
                cpos = result[1]

        else:
            l, cpos = mov(11, encoded, cpos)
            for y in range(l):
                result = decode(encoded, cpos)
                v += result[0]
                cpos = result[1]
    return v, cpos

def init():
    table = {
            '0':'0000', 
            '1':'0001',
            '2':'0010',
            '3':'0011',
            '4':'0100',
            '5':'0101',
            '6':'0110',
            '7':'0111',
            '8':'1000',
            '9':'1001',
            'A':'1010',
            'B':'1011',
            'C':'1100',
            'D':'1101',
            'E':'1110',
            'F':'1111'
            }
    swap = ""
    fin = open("input.txt", "r").read().strip()
    #fin = input("")
    for i in fin:
        swap += table[i]
    return swap

def main():
    encoded = init()
    #print(encoded)
    print(decode(encoded, 0)[0])

    
    

main()
