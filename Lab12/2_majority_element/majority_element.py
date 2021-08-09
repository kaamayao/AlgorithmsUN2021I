import sys

def get_majority_element(a, left, right):
    if len(a) == 1:
        return a[0]
    elif len(a) == 0:
        return None
    half = len(a) // 2
    left = get_majority_element(a[0:half],left,right)
    right = get_majority_element(a[half:],left,right)
    if left == right:
        return left
    if a.count(right) > half:
        return right
    if a.count(left) > half:
        return left
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
