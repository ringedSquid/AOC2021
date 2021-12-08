#looked up some math, and the fuel consumption is like a factorial but with\n
#addition, so I looked up "factorial but with addition" and I found:\n
#f(x) = (f**2 + f)/2
def fcon(n):
    return (n**2 + n)/2

def fval(n, array):
    x = 0
    for i in range(len(array)):
        x += fcon(abs(array[i]-n))
    return x

fin = open("input.txt", "r")
fin = [int(x) for x in fin.read().split(",")]
av = int(round(sum(fin)/len(fin), 0))
hm = fval(av, fin)
#originally just plain brute force, but I made it faster?\n
#its like a ball on a hill, its gonna go down to the lowest point
if hm > fval(av+1, fin):
    tm = 0
    for i in range(1, max(fin)-av):
        tm = fval(av+i, fin)
        if tm < hm:
            hm = tm
        else:
            break

elif hm > fval(av-1, fin):
    tm = 0
    for i in range(1, av):
        tm = fval(av-i, fin)
        if tm < hm:
            hm = tm
        else:
            break

print(hm)
