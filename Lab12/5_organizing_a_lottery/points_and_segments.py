# Uses python3
import sys
from functools import cmp_to_key

def segment_cmp(a, b):
    if a['point']> b['point']:
        return 1
    elif a['point']< b['point']:
        return -1
    else:
        return 0

def countBefore(segments, point):
    count = 0

def fast_count_segments(starts, ends, points):
    starts.sort()
    ends.sort()
    res = []
    for point in points:
        count = 0
        countS = True
        countE = True
        i=0
        while (countS or countE) and i<len(starts):
            countS = countS and (starts[i] < point)
            countE = countE and (ends[i] < point)
            if countS:
                count +=1
            if countE:
                count -=1
            i +=1
        res.append(count)
    return res

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
