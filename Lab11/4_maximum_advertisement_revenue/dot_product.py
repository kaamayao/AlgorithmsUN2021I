import sys

def max_dot_product(a, b):
    res = 0
    a.sort()
    b.sort(key = abs, reverse = True)
    for x in b:
        num = 0
        if x >= 0:
            num = a.pop()
        if x < 0:
            num = a.pop(0)
        res += num*x

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

