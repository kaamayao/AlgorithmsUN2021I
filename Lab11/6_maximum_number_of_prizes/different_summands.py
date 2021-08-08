# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i = n
    l = 1

    while i>0:
        if i<= (2*l):
            summands.append(i)
            i = i-i
        else:
            summands.append(l)
            i = i-l
        l = l+1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
