def literal(packet):
    number = ""
    packet = packet[6:len(packet)]
    for i in range(len(packet)//5):
        number += packet[(i*5)+1:(i*5)+5]

    number = int(number, 1)
    return number
#literal("110100101111111000101000")
def findsub(encoded):
    v = int(encoded[0:3], 2)
    t = int(encoded[3:6], 2)
    i = int(encoded[7])
    if v == 4:
        

    
def decode(encoded):
    sm = 0
    v = int(encoded[0:3], 2)
    t = int(encoded[3:6], 2)
    i = int(encoded[7])
    if v == 4:
        sm += literal(encoded)
    else:
        packet = ""
        packet += v + t + i
        if i = 0:
            packet += encoded[8:23]
            l = int(encoded[8:23], 2)
            packet += encoded[23:23+l]
            sm += decode(packet)
        elif i = 1:
            l = int(encoded[8:19], 2)




    
    


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
    fin = open("tnput.txt", "r").read().strip()
    for i in fin:
        swap += table[i]
    return swap

def main():
    encoded = init()
    decode(encoded)
    
    

main()
