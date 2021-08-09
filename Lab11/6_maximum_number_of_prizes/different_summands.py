# Uses python3
import sys

def optimal_summands(n):
    summands = []
    max_n = n
    min_n = 1

    while max_n  >0:
        if max_n <= (2*min_n):
            summands.append(max_n)
            max_n = max_n-max_n
        else:
            summands.append(min_n)
            max_n = max_n-min_n
        min_n = min_n+1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')