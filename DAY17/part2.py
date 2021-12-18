def check(xb, yb, xv, yv):
    x, y = 0, 0
    while x <= xb[1] and y >= yb[0]:
        x += xv; y += yv
        if xb[0] <= x <= xb[1] and yb[0] <= y <= yb[1]:
            return True
        if xv != 0: 
            xv -= 1 
        yv -= 1

    return False

def bash(xb, yb):
    n = 0
    for i in range(0, xb[1]+1):
        for y in range(yb[0]-1, 250):
            if check(xb, yb, i, y) == True:
                n += 1
    return n
    


def init():
    fin = [int(i) for i in open("input.txt", "r").read().split()]
    xb = [fin[0], fin[1]]
    yb = [fin[2], fin[3]]
    return xb, yb

def main():
    xb, yb = init()
    print(bash(xb, yb))
    



main()
