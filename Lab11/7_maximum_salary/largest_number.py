import sys
from functools import cmp_to_key

def base_compare(x,y):
    x_first_num = int(x+y)
    y_first_num = int(y+x)
    if x_first_num > y_first_num:
        return -1
    elif x_first_num < y_first_num:
        return 1
    else:
        return 0

def largest_number(a):
    a.sort(key=cmp_to_key(base_compare))
    return ''.join(a)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

