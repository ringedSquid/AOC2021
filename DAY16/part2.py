def mov(n, encoded, cpos):
    cpos += n
    return int(encoded[cpos-n:cpos], 2), cpos, encoded[cpos-n:cpos]

def tvalu(t, subs):
    match t:
        case 0:
            return sum(subs)
        case 1:
            n = subs[0]
            for i in range(1, len(subs)): n *= subs[i]
            return n
        case 2:
            return min(subs)
        case 3:
            return max(subs)
        case 5:
            if subs[0] > subs[1]: return 1
            else: return 0
        case 6:
            if subs[0] < subs[1]: return 1
            else: return 0
        case 7:
            if subs[0] == subs[1]: return 1
            else: return 0


def decode(encoded, cpos):
    v, cpos, _ = mov(3, encoded, cpos)
    t, cpos, _ = mov(3, encoded, cpos)
    if t == 4:
        buffer = ""
        while encoded[cpos] == "1":
            result = mov(5, encoded, cpos)
            cpos = result[1]
            buffer += result[2][1:]
        #last set
        result = mov(5, encoded, cpos)
        cpos = result[1]
        buffer += result[2][1:]
        return int(buffer, 2), cpos

    else:
        subs = []
        i, cpos, _ = mov(1, encoded, cpos)
        if i == 0:
            l, cpos, _  = mov(15, encoded, cpos)
            r = cpos
            while cpos - r < l:
                result = decode(encoded, cpos)
                subs.append(result[0])
                cpos = result[1]
        else:
            l, cpos, _  = mov(11, encoded, cpos)
            for y in range(l):
                result = decode(encoded, cpos)
                subs.append(result[0])
                cpos = result[1]
        
        return tvalu(t, subs), cpos
    

        

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
