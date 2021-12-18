def check(xb, yb, xv, yv):
    x, y = 0, 0
    mh = 0
    while x <= xb[1] and y >= yb[1]:
        x += xv; y += yv; yv -= 1
        if xv != 0: 
            xv -= 1
        if y > mh:
            mh = y
        if xb[0] <= x <= xb[1] and yb[0] <= y <= yb[1]:
            return True, mh

    return False, mh


def init():
    fin = [int(i) for i in open("input.txt", "r").read().split()]
    xb = [fin[0], fin[1]]
    yb = [fin[2], fin[3]]
    return xb, yb

def main():
    xb, yb = init()
    i = yb[0]
    #If only I was cracked at math :(
    print(((-i-1)*-i)//2)

main()
