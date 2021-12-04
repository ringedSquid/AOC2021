def binc(array, n):
    for i in range(len(array)):
        for y in range(len(array[i])):
            if array[i][y] == n:
                array[i][y] = 'B'

    return array

def cheb(array):
    varray = []
    for i in range(len(array)):
        x = []
        for y in range(len(array[i])):
            x.append(array[y][i])
        varray.append(x)

    for i in range(len(array)):
        if all(x == 'B' for x in array[i]) or all(x == 'B' for x in varray[i]):
            return True

    return False

def addu(array):
    sum = 0
    for i in range(len(array)):
        for y in range(len(array[i])):
            if array[i][y] != 'B':
                sum += array[i][y]
    return sum

def init():
    #FUCK THIS INPUT BULLSHIT
    fin = open("input.txt", "r")
    fin = fin.read().split("\n")
    numbers = []
    swap = []
    for i in range(len(fin)):
        if fin[i] != '':
            swap.append(fin[i])

    fin = swap
    swap = []
    numbers = [int(x) for x in fin[0].split(",")]

    for i in range(1, len(fin)):
        swap.append([int(x) for x in fin[i].split()])
    
    fin = swap
    swap = []

    for i in range(len(fin)//5):
        swap.append([])
        for y in range(5):
            swap[i].append(fin[(i*5)+y])

    fin = swap
    swap = []
    return numbers, fin

def main():
    winners = []
    values = init()
    numbers = values[0]
    grids = values[1]
    gridlen = len(grids)
    for i in range(len(numbers)):
        swap = []
        for y in range(len(grids)):
            grids[y] = binc(grids[y], numbers[i])
            if cheb(grids[y]) == True:
                winners.append(grids[y])
            else:
                swap.append(grids[y])

            if len(winners) == gridlen:
                return addu(grids[y])*numbers[i];

        grids = swap 
           
if __name__ == "__main__":
    result = main()
    print(result)

